# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.options
from application import Application

from tornado.options import define,options

define('port', default=8888, help='run on the given port', type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()


#  172.17.53.170