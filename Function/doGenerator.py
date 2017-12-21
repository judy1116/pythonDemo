L=[x*x for x in range(10)]
G=(x*x for x in range(10))
print(L)
print(G)
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print(next(G))
#不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
for n in G:
    print(n)

#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n,a,b=0,0,1
    while n<max:
        #print(b)
        #上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib(6))


def odd():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
print(next(o))
print(next(o))

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

##########小结##########
#generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
#要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


##########练习：杨辉三角定义如下：
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
    return L

print(list(triangles()))
#def YangHui (num = 10):
#    LL = [[1]]
#    for i in range(1,num):
#        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
#    return LL
