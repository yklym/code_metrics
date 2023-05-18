from check import check_inheritance_depth

#      e -- f
#     /
# d -
#     \
#      C -- B -- A


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class F:
    pass


class E(F):
    pass


class D(C, E):
    pass


# print('Test separate classes depth-------------')
# print("depth 0", check_inheritance_depth(A))
# print("depth 1", check_inheritance_depth(B))
# print("depth 2", check_inheritance_depth(C))
# print("depth 3", check_inheritance_depth(D))
# print()
