#采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class Animal(object):
    pass
#大类：
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物
#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Runnable):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
############小结############
#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用MixIn的设计。