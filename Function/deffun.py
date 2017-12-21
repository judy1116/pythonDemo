import math #import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

def my_abs(x):
    #对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

#空函数:如果想定义一个什么事也不做的空函数，可以用pass语句：
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#def nop():
#    pass

#if age>=18:
#    pass

print(my_abs(1))
#print(my_abs('A'))

x,y=move(100, 100, 60, math.pi / 6)
print(x,y)
#但其实这只是一种假象，Python函数返回的仍然是单一值：
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r= move(100, 100, 60, math.pi / 6)
print(r)



#小结

#定义函数时，需要确定函数名和参数个数；

#如果有必要，可以先对参数的数据类型做检查；

#函数体内部可以用return随时返回函数结果；

#函数执行完毕也没有return语句时，自动return None。

#函数可以同时返回多个值，但其实就是一个tuple。

def quadratic(a,b,c):
#    if a=0:
#        raise TypeError('a必须等于0')
    x1=(-b+math.sqrt(b*b-4*a*c))/2*a
    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
    return x1,x2

result=quadratic(1,3,-4)
print(result)
    