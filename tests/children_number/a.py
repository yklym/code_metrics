from check import get_children_number

#      B -- D
#     /
# A -
#     \
#      C


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


# print('Test separate classes children--------------')
# print("children 2", get_children_number(A))
# print("children 1", get_children_number(B))
# print("children 0", get_children_number(D))
# print()
