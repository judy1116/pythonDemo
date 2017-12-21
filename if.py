#条件注意不要少写了冒号:
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#简写：只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=0
if x:
    print('True')
else:
    print('False')



s=input('birth:')
#int()转换input返回的数据类型str为int型
birth=int(s)
if birth<2000:
   print('00前')
else:
   print('00后')