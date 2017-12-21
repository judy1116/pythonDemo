print( list(range(1, 11)))

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L=[]
for x in range(1,11):
    L.append(x*x)

print(L)
#以上的方式太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L=[x*x for x in range(1,11)]

#还可以使用两层循环，可以生成全排列：
print([m+n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os #导入os模块
print([d for d in os.listdir('.')])

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])
#把一个list中所有的字符串变成小写：
L=['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#练习:如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L2= ['Hello', 'World', 18, 'Apple', None]
print([t.lower() for t in L2 if isinstance(t,str)] )
