#coding:utf-8
def add(x, y, f):
    return f(x) + f(y)

f = abs ;

sum = add(2,3,f)
print(sum);

# 高阶函数的运用
#map
List = [1, 2, 3, 4, 5, 6, 7, 8, 9] ;
r = map(f,List)

def f(x):
    return x * x 
print(r);

#reduce

def fn(x,y):
    return x * y ;

result  = reduce(fn,List)
print(result)

