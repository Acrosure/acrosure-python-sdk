import requests
import json

API_URL = "https://api.acrosure.com"

def api( path, body = None, token = None):
    try:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = "Bearer " + token
        # print("##############################")
        # print(json.dumps(body))
        # print(API_URL + path)
        # print(headers)
        # print("##############################")
        response = requests.post(API_URL + path,
            data = json.dumps(body),
            headers = headers)
        # print("RESPONSE")
        # print(response)
        if not response:
            raise Exception("no response")
        data = response.json()
        # print("DATA")
        # print(data)
        return data
    except Exception as err:
        # console.warn(err)
        error = err.args[0] 
        if hasattr(error, "get"):
            if error.get("response", {}).get("data"):
                raise Exception(error["response"]["data"])
            elif error.get("response"):
                raise Exception(error["response"])
        raise Exception(error)