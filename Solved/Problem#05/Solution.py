def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pr):
    def _car(x, y):
        return x
    print(pr(_car))

def cdr(pr):
    def _cdr(x, y):
        return y
    print(pr(_cdr))
