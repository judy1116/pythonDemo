#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names=['Mike','Bob','Tracy']
for name in names:
    print(name)

#range()函数：可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))
#range(101)就可以生成0-100的整数序列
sum=0
for x in range(101):
    sum=sum+x
print(sum)

#while
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)