from PIL import Image
im=Image.open('test.png')
print(im.format,im.size,im.mode)
#im.thumbnail((200,100))
#im.save('thumb.png','PNG')

import sys
print(sys.path)

#一是直接修改sys.path，添加要搜索的目录：
sys.path.append('/Users/michael/my_py_scripts')
#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。