import requests
import json
# const API_URL = 'https://api.phantompage.com'
# API_URL = 'http://localhost:8000'
API_URL = "https://my-json-server.typicode.com/jetarin-min/json-placeholder"

def api( path, body = None, token = None):
    try:
        print("path " + path)
        print("token " + token)
        print(body)
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = "Bearer " + token
        response = requests.get(API_URL + path,
            # data = json.dumps(body),
            headers = headers)
        if not response:
            raise Exception("no response")
        data = response.json()
        if data.get("status") != "ok":
            raise Exception(data)
        return data["data"]
    except Exception as err:
        # console.warn(err)
        error = err.args[0] 
        if hasattr(error, "get"):
            if error.get("response", {}).get("data"):
                raise Exception(error["response"]["data"])
            elif error.get("response"):
                raise Exception(error["response"])
        raise Exception(error)