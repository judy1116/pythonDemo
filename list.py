classmates=['Mike','Bob','Tracy']
print(classmates)
#用len()函数可以获得list元素的个数：
print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素;
#以此类推-2，-3表示倒数第二第三
print(classmates[-1])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('adam')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)
#要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1]='Sarah'
print(classmates)
#list里面的元素的数据类型也可以不同
L=['Apple',123,True]
#list元素也可以是另一个list
s=['python','java',['asp','php'],'scheme']
print(len(s))
#拆开写
p=['asp','php']
s=['python','java',p,'scheme']
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到
print(p[1])
print(s[2][1])
#如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L=[]
print(len(L))