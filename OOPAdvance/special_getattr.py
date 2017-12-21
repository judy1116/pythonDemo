#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):
    def __init__(self):
        self.name='Michael'
    #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
    #注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
s=Student()
print(s.name)
print(s.score)
#错误信息很清楚地告诉我们，没有找到score这个attribute。
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
#print(s.age)
#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#举个例子：
#现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#http://api.server/user/friends
#http://api.server/user/timeline/list
#如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
print(Chain().status.user.timeline.list)
#这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
#还有些REST API会把参数放到URL中，比如GitHub的API：
#调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
print(Chain().user('michael').repos)