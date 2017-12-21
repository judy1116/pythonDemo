a = 'judy'
print(a)
b = a
a = 'ricky'
print(b)

print('Hello,%s' % 'world')
print('Hi,%s,you have $%d.' % ('world',100000))
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%d-%01d' % (3, 1))
print('%.2f' % 3.1415926)
print('%.1f' % 3.1415926)
#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)