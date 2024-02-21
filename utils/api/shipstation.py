
import os


SHIPSTATION_BASE_URL = 'https://ssapi.shipstation.com/'


def get_ss_request_headers():
    auth_token = os.getenv('SS_AUTH_TOKEN', default=None)

    partner_key = os.getenv('SS_X_PARTNER_KEY', default=None)

    if auth_token is None or partner_key is None:
        raise ValueError('ShipStation API credentials not found')

    return {
        'Authorization': auth_token,
        'X-Partner': partner_key
    }


def get_ss_orders():

    headers = get_ss_request_headers()

    return headers
