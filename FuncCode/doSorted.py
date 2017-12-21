#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36,5,-12,9,-21]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36,5,-12,9,-21],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower, reverse=True))

#练习
#假设我们用一组tuple表示学生名字和成绩：
from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=itemgetter(0)))
print(sorted(L,key=itemgetter(1),reverse=True))