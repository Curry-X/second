
import functools

def log(func=''):
        def decorators(func): 
            @functools.wraps(func)
            def w(*args,**kw):
                print('Curry_Xu 来也！！！%s'%(func.__name__))

 # coding: utf-8


import functools

def log(nihao=''):
        def decorators(func): 
            @functools.wraps(func)
            def w(*args,**kw):
                print('Curry_Xu 来也！！！%s %s'%(func.__name__, nihao))
                func(*args,**kw)
                print("哦吼，拜拜~~~")
            return w 
        return decorators  
      
    
@log()
def f():
    print("我是") #log()(f)

@log('nishi')
def nwo():
    x=12
    y=6
    z=y+x
    print(z)# log('nishi')(nwo)

f()
nwo()