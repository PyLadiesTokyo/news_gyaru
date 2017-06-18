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
    1.有効なドメインか判断する。
    2.有効なドメインの場合はそのドメインにひもづくカテゴリを返却する
    (現在は産経新聞(国際政治)：WORLD_NEWS のみ)
    """

    def post(self):
        # 送られてきたUrlからドメインを切り出す
        json = tornado.escape.json_decode(self.request.body)
        url = json['url']
        print('TargetUrl : ' + url)
        print(url.find('www.sankei.com/world/news/'))

        if url.find('www.sankei.com/world/news/') >= 0:
            # カテゴリを返却する
            json['category'] = 'WORLD_NEWS'
            self.write(json)

        else:
            # ドメインが産経以外の場合はcategoryを返却しない
            self.write(json)




def main():
    parse_command_line()
    application = tornado.web.Application(
        [
            (r'/test', TestHandler),
            (r'/url', UrlHandler)
        ]
    )
    application.listen(options.port)
    print('接続OK')
    print(u'http://サーバドメイン:' + str(options.port) + u'/')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
