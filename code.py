# hw 2
%python
def cube(n) :
    n = n**3
    return n
    
def by_five(*arg) :
    if arg % 5 == 0 :
        return cube()
    else:
        return False
%timeit cube(90)


%cython
def cube(int n) :
    n = n**3
    return n
    
def by_five(*arg) :
    if arg % 5 == 0 :
        return cube()
    else:
        return False
timeit("cube(90))
