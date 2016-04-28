#-*- coding:utf-8 -*-
def thread1():
    for x in range(4):
        yield  x
        
 
def thread2():
    for x in range(4,8):
        yield  x
        
 
threads=[]
threads.append(thread1())
threads.append(thread2())
 
 
# def run(threads): #写这个函数，模拟线程并发
#     pass
def run(threads):
    for t in threads:
        try:
            print t.next()
        except StopIteration:
            pass
        else:
            threads.append(t)
 
run(threads)