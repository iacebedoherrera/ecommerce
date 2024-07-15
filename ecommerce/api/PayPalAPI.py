import base64, os, requests, dotenv
import reflex as rx



# PAYPAL Constants
dotenv.load_dotenv()
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.environ.get("PAYPAL_CLIENT_SECRET")
PAYPAL_BASE_URL = os.environ.get("PAYPAL_BASE_URL")


class OrderBody(rx.Model):
    cart: str
    total_amount: str


class PayPalAPI:
    
    def generateAccessToken(self):
        if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
            raise ValueError('No hay credenciales de PayPal válidas')
        
        auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
        auth = base64.b64encode(auth.encode()).decode('utf-8')

        response = requests.post(
            f"{PAYPAL_BASE_URL}/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            headers={"Authorization": f"Basic {auth}"}
        )

        data = response.json()
        return data['access_token']


    def create_order(self, orderBody: OrderBody):
        access_token = self.generateAccessToken()
        url = f"{PAYPAL_BASE_URL}/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "EUR",
                        "value": orderBody.total_amount
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        return requests.post(url, headers=headers, json=payload)
    
    def capture_order(self, order_id):
        access_token = self.generateAccessToken()
        url = f"{PAYPAL_BASE_URL}/v2/checkout/orders/{order_id}/capture"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        return requests.post(url, headers=headers)
