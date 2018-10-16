import tornado.ioloop
import tornado.web
from acrosure_sdk import AcrosureClient
import os
import json

from data import APP_DATA

acrosure_client = AcrosureClient(
  token = os.environ.get('TEST_SECRET_TOKEN')
)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href=\"/test-sdk\"><button>Test</button></a>")

class SdkHandler(tornado.web.RequestHandler):
    def get(self):
        print("start")
        print("-------------------------------")
        resp = acrosure_client.application.create(
            product_id = APP_DATA["product_id"],
            basic_data = APP_DATA["basic_data"]
        )
        print("create:")
        print(resp)
        print("-------------------------------")
        application_id = resp["data"]["id"]
    
        resp = acrosure_client.application.get_packages(application_id)
        print("get-packages:")
        print(resp)
        print("-------------------------------")
        package_code = resp["data"][0]["package_code"]

        resp = acrosure_client.application.select_package(
            application_id = application_id,
            package_code = package_code
        )
        print("select-package:")
        print(resp)
        print("-------------------------------")
        
        resp = acrosure_client.application.update(
            application_id = application_id,
            basic_data = APP_DATA["basic_data"],
            package_options = APP_DATA["package_options"],
            additional_data = APP_DATA["additional_data"]
        )
        print("update:")
        print(resp)
        print("-------------------------------")

        resp = acrosure_client.application.confirm(application_id)
        print("confirm:")
        print(resp)
        print('===============================')
        self.write(json.dumps(resp))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test-sdk", SdkHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
