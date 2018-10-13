from acrosure_sdk import AcrosureClient
import tornado.ioloop
import tornado.web

acrosure_client = AcrosureClient(
  token = "tokn_sample_secret"
)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        resp = acrosure_client.application.create(product_id = "prod_ta")
        print(resp)
        self.write("ok")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
