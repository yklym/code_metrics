from check import get_class_pof_data, get_pof


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


class C(D):
    # inherits  all methods

    pass


class E(A):
    #  adds new methods
    def quack():
        pass

    def woof():
        pass


# print('Test separate classes depth-------------')
# print("pof a", get_pof(A), get_class_pof_data(A))
# print("pof b", get_pof(B), get_class_pof_data(B))
# print("pof c", get_pof(C), get_class_pof_data(C))
# print("pof d", get_pof(D), get_class_pof_data(D))
# print("pof e", get_pof(E), get_class_pof_data(E))
