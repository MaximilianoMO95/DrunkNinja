import requests
import logging
from urllib.parse import parse_qs

from django.contrib.admin.options import method_decorator
from django.contrib.auth.views import login_required
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site

from .conf import settings

from apps.products.models import Basket

@method_decorator(login_required, name='dispatch')
class RedirectPaymentView(View):
    template_name = 'payment/checkout.html'

    def get(self, request):
            basket_items = Basket.objects.filter(user=self.request.user)

            order_id = 'drunkNinja-order123'
            order_total_amount = basket_items.total_sum()

            baseurl = request.scheme + '://' + get_current_site(request).domain
            session_id = request.session.session_key

            webpay = WebpayAPI()
            response_data = webpay.create_transaction(baseurl, order_total_amount, order_id, session_id)

            if response_data:
                url = response_data['url']
                token = response_data['token']

                return render(request, self.template_name, { 'url': url, 'token_ws': token, 'total_amount': order_total_amount })
            else:
                return HttpResponse('Failed to create Webpay transaction')


@method_decorator(login_required, name='dispatch')
class PaymentResultView(View):
    template_name = 'payment/result.html'

    def get(self, request):
        webpay = WebpayAPI()
        query_params = parse_qs(request.GET.urlencode())

        reject_token = 'TBK_TOKEN'
        if reject_token in query_params:
            return render(request, self.template_name, { 'pay_status': 'PAGO CANCELADO' })

        token = 'token_ws'
        if token in query_params:
            token = query_params[token][0]
        
        response_data = webpay.commit_transaction(token)
        if response_data:
            pay_status = response_data['status']
            return render(request, self.template_name, { 'pay_status': pay_status })
        else:
            return HttpResponse('Failed to confirm Webpay transaction')


class WebpayAPI:
    headers= {
        'Tbk-Api-Key-Id': settings.WEBPAY_COMMERCE_CODE,
        'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET_KEY,
        'Content-Type': 'application/json',
    }

    def create_transaction(self, baseurl, amount, order_id, session_id):
        endpoint = settings.WEBPAY_API_URL + '/transactions' 

        data = {
            'buy_order': order_id,
            'session_id': session_id,
            'amount': amount,
            'return_url': baseurl + '/payment/result',
        }

        try:
            response = requests.post(
                endpoint,
                json= data,
                headers=self.headers,
                timeout=(5, 30)
            )

            if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
                return response.json()
            else:
                logging.info(f"INFO: [webpay] Create transaction response code: [{ response.status_code }]")
                return None 

        except requests.exceptions.RequestException as e:
            logging.error(f"ERROR: [webpay] making API request: {e}")
            return None

    
    def commit_transaction(self, token):
        endpoint = settings.WEBPAY_API_URL + f'/transactions/{ token }'

        try:
            response = requests.put(
                endpoint,
                headers=self.headers
            )

            if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
                return response.json()
            else:
                logging.info(f"INFO: [webpay] Commit transaction response code: [{response.status_code}]")
                return None 

        except requests.exceptions.RequestException as e:
            logging.error(f"ERROR: [webpay] making API request: {e}")
            return None
