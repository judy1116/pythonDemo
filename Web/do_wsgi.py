##########运行WSGI服务##########
#负责启动WSGI服务器，加载application()函数：
#从wsgiref模块导入：
from wsgiref.simple_server import make_server
#导入我们自己编写的application
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听http请求：
httpd.serve_forever()
#确保以上两个文件在同一个目录下，然后在命令行输入python server.py来启动WSGI服务器：