from check import get_class_ahf_data
from helpers import get_class_attributes


class A:
    _nose = 1
    paw = 4
    whiskers = 2


class B(A):
    _hidden = ''
    attr1 = ''


print('Test separate classes depth-------------')
print('get_class_attributes', get_class_attributes(A), get_class_ahf_data(A))
print('get_class_attributes', get_class_attributes(B), get_class_ahf_data(B))

# print("mhf a", get_mhf(A))
# print("mhf b", get_mhf(B))
# print("mhf c", get_mhf(C))


print()
