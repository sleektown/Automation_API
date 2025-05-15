import pytest
import requests
from config import baseurl
from utils.helper import read_json_file

test_data = read_json_file(fr'data\token_data.json')
from api_requests.token_api import Auth_Token

@pytest.fixture
def test_fixture():
    params = test_data["Token_api"]["valid_creds"]
    requests = Auth_Token.token_api(baseurl, params)
    access_token = requests.get("access_token")
    yield access_token

    

    
    