class Student(object):
    def __init__(self,name):
        self.name=name
    #打印出一堆<__main__.Student object at 0x109afb190>，不好看。
    #怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
    def __str__(self):
        return 'Student object(name:%s)'%self.name
    #因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    #解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
    __repr__=__str__
print(Student('Michael'))
s=Student('jduy')
print(s)
