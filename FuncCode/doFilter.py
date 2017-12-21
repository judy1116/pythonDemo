#Python内建的filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_ood(n):
    return n%2==1

print(list(filter(is_ood,[1, 2, 4, 5, 6, 9, 10, 15])))

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

print(filter(not_empty,['A','','B',None,'C','  ']))

#用filter求素数
#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x:x%n>0
#定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it=_odd_iter()#初始序列
    while True:
        n=next(it)#返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)#构造新序列

#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
#打印1000以内的素数：
for n in primes():
    if n<1000:
        print(n)
    else:
        break


##############小结##############
#filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

##############练习##############
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
#    I,m=n,0
#    while I:
#        m=m*10+10%10
#        I=I//10
#    return(n==m)
     return str(n)==str(n)[::-1]

L=list(filter(is_palindrome,range(1,1000)))
print(L)