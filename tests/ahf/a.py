from check import get_class_ahf_data, get_ahf
from helpers import get_class_attributes


class A:
    __nose = 1
    paw = 4
    whiskers = 2


class B(A):
    __hidden = ''
    attr1 = ''


# print('Test separate classes depth-------------')

# print("mhf a", get_ahf(A))  # 0.3
# print("mhf b", get_ahf(B))  # 0.5
