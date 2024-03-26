from dotenv import load_dotenv
import os
import sys
import json
import requests_mock
import pytest
import requests

load_dotenv()

## To import the lib module
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from lib.api import get_subfeddits, get_subfeddit_info, get_comments

subfeddit_resp = json.loads(
    '{"limit": 10, "skip": 0, "subfeddits": [{"id": 1, "username": "admin_1", "title": "Dummy Topic 1", "description": "Dummy Topic 1"}, {"id": 2, "username": "admin_2", "title": "Dummy Topic 2", "description": "Dummy Topic 2"}, {"id": 3, "username": "admin_3", "title": "Dummy Topic 3", "description": "Dummy Topic 3"}]}'
)

def test_get_subfeddits_normal():
    with requests_mock.Mocker() as m:
        # test normal working of API
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddits/', json=subfeddit_resp, status_code=200)
        assert get_subfeddits() == subfeddit_resp
    
def test_get_subfeddits_non_200():
    with requests_mock.Mocker() as m:
        # test non 200 response code
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddits/', text=None, status_code=400)
        with pytest.raises(Exception) as e:
            get_subfeddits()
        assert str(e.value) == 'API Error'

def test_get_subfeddits_timed_out():
    with requests_mock.Mocker() as m:
        # test API timed out
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddits/', exc=requests.exceptions.ConnectTimeout)
        with pytest.raises(Exception) as e:
            get_subfeddits()
        assert str(e.value) == 'API Error'

subfeddit_info_resp = json.loads(
    '{"id": 1, "username": "admin_1", "title": "Dummy Topic 1", "description": "Dummy Topic 1", "limit": 10, "skip": 0, "comments": [{"id": 1, "username": "user_0", "text": "It looks great!", "created_at": 1711449247}, {"id": 2, "username": "user_1", "text": "Love it.", "created_at": 1711445647}, {"id": 3, "username": "user_2", "text": "Awesome.", "created_at": 1711442047}, {"id": 4, "username": "user_3", "text": "Well done!", "created_at": 1711438447}, {"id": 5, "username": "user_4", "text": "Looks decent.", "created_at": 1711434847}, {"id": 6, "username": "user_5", "text": "What you did was right.", "created_at": 1711431247}, {"id": 7, "username": "user_6", "text": "Thumbs up.", "created_at": 1711427647}, {"id": 8, "username": "user_7", "text": "Like it a lot!", "created_at": 1711424047}, {"id": 9, "username": "user_8", "text": "Good work.", "created_at": 1711420447}, {"id": 10, "username": "user_9", "text": "Luckily you did it.", "created_at": 1711416847}]}'
)

def test_get_subfeddit_info_normal():
    with requests_mock.Mocker() as m:
        # test normal working of API
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddit?subfeddit_id=1', json=subfeddit_info_resp, status_code=200)
        assert get_subfeddit_info(1) == subfeddit_info_resp

def test_get_subfeddit_info_None_Args():
    with requests_mock.Mocker() as m:
        # test function with no args
        with pytest.raises(Exception) as e:
            get_subfeddit_info(None)
        assert str(e.value) == 'Provide Subfeddit ID'

def test_get_subfeddit_info_non_200():
    with requests_mock.Mocker() as m:
        # test non 200 response code
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddit?subfeddit_id=43', text=None, status_code=404)
        with pytest.raises(Exception) as e:
            get_subfeddit_info(43)
        assert str(e.value) == 'API Error'

def test_get_subfeddit_info_timed_out():
    with requests_mock.Mocker() as m:
        # test API timed out
        m.get(f'http://{os.getenv('API_URL')}/api/v1/subfeddit?subfeddit_id=1', exc=requests.exceptions.ConnectTimeout)
        with pytest.raises(Exception) as e:
            get_subfeddit_info(1)
        assert str(e.value) == 'API Error'

comments_resp = json.loads(
    '{"subfeddit_id": 1, "limit": 20, "skip": 0, "comments": [{"id": 1, "username": "user_0", "text": "It looks great!", "created_at": 1711449247}, {"id": 2, "username": "user_1", "text": "Love it.", "created_at": 1711445647}, {"id": 3, "username": "user_2", "text": "Awesome.", "created_at": 1711442047}, {"id": 4, "username": "user_3", "text": "Well done!", "created_at": 1711438447}, {"id": 5, "username": "user_4", "text": "Looks decent.", "created_at": 1711434847}, {"id": 6, "username": "user_5", "text": "What you did was right.", "created_at": 1711431247}, {"id": 7, "username": "user_6", "text": "Thumbs up.", "created_at": 1711427647}, {"id": 8, "username": "user_7", "text": "Like it a lot!", "created_at": 1711424047}, {"id": 9, "username": "user_8", "text": "Good work.", "created_at": 1711420447}, {"id": 10, "username": "user_9", "text": "Luckily you did it.", "created_at": 1711416847}, {"id": 11, "username": "user_10", "text": "Proud of you.", "created_at": 1711413247}, {"id": 12, "username": "user_11", "text": "Enjoy!", "created_at": 1711409647}, {"id": 13, "username": "user_12", "text": "It looks great! It looks great!", "created_at": 1711406047}, {"id": 14, "username": "user_13", "text": "It looks great! Love it.", "created_at": 1711402447}, {"id": 15, "username": "user_14", "text": "It looks great! Awesome.", "created_at": 1711398847}, {"id": 16, "username": "user_15", "text": "It looks great! Well done!", "created_at": 1711395247}, {"id": 17, "username": "user_16", "text": "It looks great! Looks decent.", "created_at": 1711391647}, {"id": 18, "username": "user_17", "text": "It looks great! What you did was right.", "created_at": 1711388047}, {"id": 19, "username": "user_18", "text": "It looks great! Thumbs up.", "created_at": 1711384447}, {"id": 20, "username": "user_19", "text": "It looks great! Like it a lot!", "created_at": 1711380847}]}'
)

def test_get_comments_normal():
    with requests_mock.Mocker() as m:
        # test normal working of API
        m.get(f'http://{os.getenv('API_URL')}/api/v1/comments?subfeddit_id=1', json=comments_resp, status_code=200)
        assert get_comments(1) == comments_resp

def test_get_comments_None_Args():
    with requests_mock.Mocker() as m:
        # test function with no args
        with pytest.raises(Exception) as e:
            get_comments(None)
        assert str(e.value) == 'Provide Subfeddit ID'

def test_get_comments_non_200():
    with requests_mock.Mocker() as m:
        # test non 200 response code
        m.get(f'http://{os.getenv('API_URL')}/api/v1/comments?subfeddit_id=43', text=None, status_code=404)
        with pytest.raises(Exception) as e:
            get_comments(43)
        assert str(e.value) == 'API Error'

def test_get_comments_timed_out():
    with requests_mock.Mocker() as m:
        # test API timed out
        m.get(f'http://{os.getenv('API_URL')}/api/v1/comments?subfeddit_id=1', exc=requests.exceptions.ConnectTimeout)
        with pytest.raises(Exception) as e:
            get_comments(1)
        assert str(e.value) == 'API Error'
