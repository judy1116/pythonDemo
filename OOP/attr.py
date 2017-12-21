#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student('Bob')
s.score=90

#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student2(object):
    name = 'Student2'
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s2=Student2()# 创建实例s2
print(s2.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student2.name) # 打印类的name属性
s2.name = 'Michael' # 给实例绑定name属性
print(s2.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student2.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s2.name # 如果删除实例的name属性
print(s2.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
