#!/usr/bin/python
# Filename: objvar.py
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print ('(Initializing %s)' % self.name)

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print ('%s says bye.' % self.name)

        Person.population -= 1

        if Person.population == 0:
            print ('I am the last one.')
        else:
            print ('There are still %d people left.' % Person.population)

    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print ('Hi, my name is %s.' % self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print ('I am the only person here.')
        else:
            print ('We have %d persons here.' % Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

# 如果你使用的数据成员名称以 双下划线前缀 比如__privatevar，Python的名称,管理体系会有效地把它作为私有变量。
# 这样就有一个惯例，如果某个变量只想在类或对象中使用，就应该以单下划线前缀。而其他的名称都将作为公共的，可以被其他类/对象使用。
# 记住这只是一个惯例，并不是Python所要求的（与双下划线前缀不同）。