from dotenv import load_dotenv
import os
import sys
import json
import requests_mock
import pytest

load_dotenv()

## To import the lib module
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from lib.api import get_subfeddits

subfeddit_resp = json.loads(
    '{"limit": 10, "skip": 0, "subfeddits": [{"id": 1, "username": "admin_1", "title": "Dummy Topic 1", "description": "Dummy Topic 1"}, {"id": 2, "username": "admin_2", "title": "Dummy Topic 2", "description": "Dummy Topic 2"}, {"id": 3, "username": "admin_3", "title": "Dummy Topic 3", "description": "Dummy Topic 3"}]}'
)

def test_get_subfeddits_normal():
    with requests_mock.Mocker() as m:
        # test normal working of API
        m.get('http://{}/api/v1/subfeddits/'.format(os.getenv('API_URL')), json=subfeddit_resp, status_code=200)
        assert get_subfeddits() == subfeddit_resp
    
def test_get_subfeddits_non_200():
    with requests_mock.Mocker() as m:
        # test non 200 response code
        m.get('http://{}/api/v1/subfeddits/'.format(os.getenv('API_URL')), text=None, status_code=400)
        with pytest.raises(Exception) as e:
            get_subfeddits()
        assert str(e.value) == 'API Error'
        

