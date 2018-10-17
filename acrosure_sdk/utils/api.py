import os
import requests
import json

API_URL = "https://api.acrosure.com"

def api( path, body = None, token = None, api_url = None):
    try:
        if not api_url:
            api_url = API_URL
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = "Bearer " + token
        response = requests.post(api_url + path,
            data = json.dumps(body),
            headers = headers)
        data = response.json()
        return data
    except Exception as err:
        error = err.args[0] 
        if hasattr(error, "get"):
            if error.get("response", {}).get("data"):
                raise Exception(error["response"]["data"])
            elif error.get("response"):
                raise Exception(error["response"])
        raise Exception(error)