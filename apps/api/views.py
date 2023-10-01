from rest_framework import generics
from apps.products.models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        product = Product.objects.filter(pk=product_id)

        return product
