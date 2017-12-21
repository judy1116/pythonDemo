#高级语言通常都内置了一套try...except...finally...的错误处理机制
class some_function():
    pass

#def foo():
#    r=some_function()
#    if r==(-1):
#        return(-1)
    #do something
#    return r

#def bar():
#    r=foo()
#    if r==(-1):
#        print('Error')
#    else:
#        pass

try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('except:',e)
#此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
else:
    print('no error!')
finally:
    print('finally...')
print('END')
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
#从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行。然后，程序继续按照流程往下走。
#try:
#    foo()
#except ValueError as e:
#    print('ValueError')
#except UnicodeError as e:
#    print('UnicodeError')
#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
#Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
#也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。    