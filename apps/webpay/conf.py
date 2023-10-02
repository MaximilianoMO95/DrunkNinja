import dotenv
import os

dotenv.load_dotenv()

class Settings:
    WEBPAY_INTEGRATION_TYPE = os.getenv('WEBPAY_INTEGRATION_TYPE')

    WEBPAY_URL = 'https://webpay3gint.transbank.cl'
    WEBPAY_API_URL = WEBPAY_URL + '/rswebpaytransaction/api/webpay/v1.2'

    WEBPAY_SECRET_KEY = os.getenv('WEBPAY_SECRET_KEY')
    WEBPAY_COMMERCE_CODE = os.getenv('WEBPAY_COMMERCE_CODE')

    def __init__(self):
        if self.WEBPAY_INTEGRATION_TYPE != 'TEST':
            self.WEBPAY_URL = 'https://webpay3g.transbank.cl'

        if not self.WEBPAY_SECRET_KEY or not self.WEBPAY_COMMERCE_CODE:
            raise ValueError("WEBPAY_SECRET_KEY and WEBPAY_COMMERCE_CODE must be defined in your .env file.")

settings = Settings()
