import pytest
import requests
from config import baseurl



class Auth_Token:

    def token_api(baseurl, params):
        
        url = baseurl + "/token"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data= params, headers= headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get token: {response.status_code} , {response.text}")