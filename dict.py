#dict就是第二种实现方式:给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
d={'Mike':95,'Bob':75,'Tracy':85}
print(d['Mike'])

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam']=67
print(d['Adam'])

d['Jack'] = 90
d['Jack'] = 88
print(d['Jack'])

#通过in判断key是否存在
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas',-1))

#移除一个key
d.pop('Bob')
print(d)

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：