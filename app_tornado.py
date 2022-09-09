import tornado.ioloop
import tornado.web
import time
from datetime import datetime
import asyncio

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.now().strftime('%H:%M:%S')
        print(f"iniciando {now}")
        #bloqueante
        time.sleep(1)
        #await asyncio.sleep(1)
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()