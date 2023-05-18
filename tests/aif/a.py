from check import get_aif


class A:
    meow = 1
    bark = 2


class B(A):
    # inherits and overrides all methods

    meow = 1
    bark = 2


class C(A):
    # inherits  all methods
    pass


class D(A):
    # inherits, overrides and adds new methods
    meow = 1
    bark = 2
    quack = 3
    woof = 4


class E(A):
    #  adds new methods
    quack = 3
    woof = 4


# print('Test separate classes depth-------------')
print("aif a", get_aif(A))
print("aif b", get_aif(B))
print("aif c", get_aif(C))
print("aif d", get_aif(D))
print("aif e", get_aif(E))
