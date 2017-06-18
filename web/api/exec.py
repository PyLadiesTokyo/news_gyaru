#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options, parse_command_line

define('port', default=8888, help='run on the given port', type=int)


class TestHandler(tornado.web.RequestHandler):
    """
    接続確認用ハンドラ
    """

    def get(self):
        test_json = {'url': 'http://xxx.co.jp/foo/1234bar.html'}
        self.write(test_json)


class UrlHandler(tornado.web.RequestHandler):
    """
    url1からカテゴリを抽出する
    """

    def post(self):
        # TODO 送られてきたUrlからドメインを切り出す

        # TODO ドメインが産経だったらカテゴリを返却する
        # TODO ドメインが産経以外の場合はcategoryを返却しない

        # TODO リターン値の整形
        return {'url': '送られてきたURL'}


def main():
    parse_command_line()
    application = tornado.web.Application(
        [
            (r"/test", TestHandler),
            (r"/url", UrlHandler)
        ]
    )
    application.listen(options.port)
    print("接続OK")
    print(u"http://サーバドメイン:" + str(options.port) + u"/")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
