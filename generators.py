def gen():
    a=10
    yield a + 1
a=gen()
next(a)