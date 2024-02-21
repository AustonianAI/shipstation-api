
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

from typing import List

from models.shipstation.order import Order


SHIPSTATION_BASE_URL = 'https://ssapi.shipstation.com'


def get_ss_request_headers():
    auth_token = os.getenv('SS_AUTH_TOKEN', default=None)
    partner_key = os.getenv('SS_X_PARTNER_KEY', default=None)

    if auth_token is None or partner_key is None:
        raise ValueError('ShipStation API credentials not found')

    return {
        'Authorization': auth_token,
        'X-Partner': partner_key
    }


def get_configured_http_session():
    retry_strategy = Retry(
        total=3,  # Total number of retries to allow
        status_forcelist=[429],  # A set of integer HTTP status codes that we should force a retry on
        backoff_factor=1  # A backoff factor to apply between attempts after the second try
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    return http


def get_ss_orders(**kwargs) -> List[Order]:
    headers = get_ss_request_headers()
    pageSize = 500
    all_orders = []

    http = get_configured_http_session()

    params = {
        'pageSize': pageSize,
        'orderStatus': 'awaiting_shipment'
    }
    params.update(kwargs)
    params['page'] = 1

    response = http.get(f'{SHIPSTATION_BASE_URL}/orders', headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    data = response.json()
    total_pages = data.get('pages', 0)

    # Process the orders from the first page
    orders = data.get('orders', [])
    all_orders.extend([Order.parse_obj(order) for order in orders])

    # Fetch subsequent pages if they exist
    if total_pages > 1:
        for page in tqdm(range(2, total_pages + 1), desc="Fetching Orders", initial=1, total=total_pages):
            params['page'] = page
            response = http.get(f'{SHIPSTATION_BASE_URL}/orders', headers=headers, params=params)

            if response.status_code != 200:
                raise Exception(f"Request failed with status {response.status_code}")

            data = response.json()
            orders = data.get('orders', [])
            all_orders.extend([Order.parse_obj(order) for order in orders])

    return all_orders
