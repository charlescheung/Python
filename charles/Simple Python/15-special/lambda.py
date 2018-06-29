#!/usr/bin/python
# Filename: lambda.py
def make_repeater(n):
    return lambda s: s*n
twice = make_repeater(2)
print (twice('word'))
print (twice(5))


>>> exec 'print "Hello World"'
>>> eval('2*3')

>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AssertionError


repr函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。注意，在大多数时候有eval(repr(object)) == object。
>>> i = []
>>> i.append('item')
>>> `i`
"['item']"
>>> repr(i)
"['item']"
基本上，repr函数和反引号用来获取对象的可打印的表示形式。你可以通过定义类的__repr__方法来控制你的对象在被repr函数调用的时候返回的内容。