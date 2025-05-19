import pytest
import requests
from config import baseurl



class Auth_Token:

    def token_api(baseurl, params):
        
        try:
            url = baseurl + "/token"
            headers = {
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = requests.post(url, data= params, headers= headers)
            status_code = response.status_code
            json_response = response.json()
            print("\n",url," Response Time: ", response.elapsed.total_seconds())
            if status_code != 200:
                return {"status_code": status_code, "json_data": json_response}
            return json_response
        except Exception as e:
            print(f"\nError occurred: {e}")
            