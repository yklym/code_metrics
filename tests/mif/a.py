from check import get_mif


class A:
    def meow():
        pass

    def bark():
        pass


class B(A):
    # inherits and overrides all methods

    def meow():
        pass

    def bark():
        pass


class C(A):
    # inherits  all methods

    pass


class D(A):
    # inherits, overrides and adds new methods

    def meow():
        pass

    def bark():
        pass

    def quack():
        pass

    def woof():
        pass


class E(A):
    #  adds new methods
    def quack():
        pass

    def woof():
        pass


# print('Test separate classes mif-------------')
# print("mif a", get_mif(A))
# print("mif b", get_mif(B))
# print("mif c", get_mif(C))
# print("mif d", get_mif(D))
# print("mif e", get_mif(E))
