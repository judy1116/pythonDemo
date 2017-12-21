d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for value in d.values():
    print(value)

for keyvalue in d.items():
    print(keyvalue)

for ch in 'ABC':
    print(ch)

from collections import Iterable
print(isinstance('abc',Iterable)) #str是否是迭代
print(isinstance([1,2,3],Iterable)) #list是否是迭代
print(isinstance(123,Iterable)) #整数是否是迭代

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)

#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)