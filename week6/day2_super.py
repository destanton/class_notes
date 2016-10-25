

class A:
    pass

    def __init__(self):
        self.ready = True


class B(A):
    pass

    def __init__(self, favorite):
        super().__init__()
        self.favorite = favorite


x = A()
print(x.ready)

y = B("jelly beans")
print(y.favorite)
print (y.ready)
