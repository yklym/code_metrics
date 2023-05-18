import tests.amf.a as test_module

from check import get_class_ahf_data

from inspect import getmembers, isclass

print('Test AHF--------------')
module_classes = getmembers(test_module, isclass)

sum_a_h = 0
sum_a_v = 0

for (class_name, _class) in module_classes:
    curr_a_h, curr_a_v = get_class_ahf_data(_class)
    sum_a_h += curr_a_h
    sum_a_v += curr_a_v

print(f'MHF of module {class_name} is [{sum_a_h / (sum_a_v)}]')
# print()
