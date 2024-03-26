"""This module contains all the functions used for calling the feddit API"""

import os
import requests

class APIException(Exception):
    """Custom Exception for the API"""

def get_subfeddits():
    """Get all the subfeddits"""
    try:
        data_from_api = requests.get(
            f'http://{os.getenv('API_URL')}/api/v1/subfeddits/',
            timeout=60
        )
        if data_from_api.status_code == 200:
            return data_from_api.json()
        raise APIException('API Error')
    except (Exception,) as exc:
        raise APIException('API Error') from exc
