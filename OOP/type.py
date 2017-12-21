#判断对象类型，使用type()函数：
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
#比较两个变量的type类型是否相同:
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance([1, 2, 3], (list, tuple)))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__)
#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100
dog=MyDog()
print(len(dog))
#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()
#测试该对象的属性：
print(hasattr(obj,'x'))# 有属性'x'吗？
print(obj.x)
print(hasattr(obj,'y')) # 有属性'y'吗？
setattr(obj,'y',19)# 设置一个属性'y'
print(hasattr(obj,'y'))# 有属性'y'吗？
print(getattr(obj,'y')) # 获取属性'y'
print(obj.y)# 获取属性'y'

#如果试图获取不存在的属性，会抛出AttributeError的错误：
#getattr(obj, 'z') # 获取属性'z'
#可以传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
#也可以获得对象的方法：
print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power'))# 获取属性'power'
fn=getattr(obj,'power')#获取属性'power'并赋值到变量fn
print(fn)
fn()# 调用fn()与调用obj.power()是一样的
#########小结#########
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
#假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。