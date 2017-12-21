def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5,2))
print(power(5))
#有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Adam', 'M', city='Tianjin'))

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end()
add_end()
print( add_end())
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


#可变参数:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
#数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
#把函数的参数改为可变参数前加‘*’：
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#非可用参数前的调用方式：
#print(calc([1,2,3]))
#print(calc((1,3,5,7)))

#如果利用可变参数，调用函数的方式可以简化成这样：
print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc())
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums=[1,2,3]
print(calc(nums[0], nums[1], nums[2]))
#上面写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc(*nums))




#关键词参数：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')

extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
#上面复杂的调用可以用简化的写法：
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('Jack',24,**extra)




#命名关键字参数
def personkey(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24,  job='Engineer')
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
#def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
#    pass




#参数组合:在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)
#通过一个tuple和dict，你也可以调用上述函数：
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


################小结#####################

#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

#要注意定义可变参数和关键字参数的语法：

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。



