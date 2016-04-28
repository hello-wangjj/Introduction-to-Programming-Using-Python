#-*- coding:utf-8 -*-
import types
def gen():
    for x in xrange(4):
        tmp = yield x
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)


g=gen()
print g
print isinstance(g, types.GeneratorType)
print g.next()
print g.next()
print g.send('hello')
print g.next()
# print g.send('hello')


def mygen():
    try:
        yield 'something'
    except ValueError:
        yield 'value error'
    finally:
        print 'clean'  #一定会被执行
gg=mygen()
print gg.next() #something
print gg.throw(ValueError) #value error  clean