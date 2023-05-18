from check import get_mhf


class A:
    # half of methods are hidden
    def __meow():
        pass

    def bark():
        pass


class B():
    # all of methods are hidden

    def __meow():
        pass

    def __bark():
        pass


class C():
    # none of methods are hidden

    def meow():
        pass

    def bark():
        pass


# print('Test separate classes depth-------------')
# print("mhf a", get_mhf(A))
# print("mhf b", get_mhf(B))
# print("mhf c", get_mhf(C))
