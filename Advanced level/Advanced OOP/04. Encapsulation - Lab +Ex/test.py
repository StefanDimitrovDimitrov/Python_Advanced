class A:
    pass

class D:
    pass

class B(D):
    pass


class C(A):
    pass

class Baba(B, C):
    pass

print(Baba.__mro__)