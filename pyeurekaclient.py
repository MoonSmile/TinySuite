# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import py_eureka_client.eureka_client as eureka_client
from tornado.options import define, options
define("port", default=3333, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', 'Hello')
        self.write(username + ', Administrator User!')

if __name__ == "__main__":
	#blog.csdn.net/moshowgame
    tornado.options.parse_command_line()
    #注册eureka服务
    eureka_client.init_registry_client(eureka_server="http://10.64.140.34:8761/eureka/",
                            app_name="python-tornado-xyweb",
                            instance_port=3333)
    #获取eureka服务（有报错，先别用）
    #res = eureka_client.do_service("GRATEWAY", "/service/context/path")
    #print("result of other service" + res)
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
