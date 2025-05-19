import pytest
from api_requests.token_api import Auth_Token
from utils.helper import read_json_file
from config import baseurl

test_data = read_json_file(fr'data\token_data.json')

class TestAuthToken:

     def test_valid_auth_valid_creds(self):
          params = test_data["Token_api"]["valid_creds"]
          response = Auth_Token.token_api(baseurl, params)
          access_token = response.get("access_token")
          print(f"\nAccess Token: {access_token}")
     
     def test_auth_invalid_creds(self):
          params = test_data["Token_api"]["invalid_creds"]
          response = Auth_Token.token_api(baseurl, params)
          assert(response["status_code"] == 400)
          print(response["json_data"])
   
          