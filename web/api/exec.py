#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options, parse_command_line

define('port', default=8888, help='run on the given port', type=int)


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        #test_json = '{"url" : "http://xxxx.co.jp/foo/1234bar.html"}'
        test_json = {'url': 'http://xxx.co.jp/foo/1234bar.html'}
        self.write(test_json)


def main():
    parse_command_line()
    application = tornado.web.Application(
        [
            (r"/test", TestHandler)
            # (r"/demo", demohandler.DemoHandler)
        ]
    )
    application.listen(options.port)
    print("接続OK")
    print(u"http://サーバドメイン:" + str(options.port) + u"/")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
