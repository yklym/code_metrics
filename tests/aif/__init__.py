import tests.aif.a as test_module
from api import get_module_aif

get_module_aif(test_module)


# from check import get_class_aif_data

# from inspect import getmembers, isclass

# print('Test AIF--------------')
# module_classes = getmembers(test_module, isclass)

# sum_a_i = 0
# sum_a_a = 0

# for (class_name, _class) in module_classes:
#     curr_a_i, curr_a_a = get_class_aif_data(_class)
#     sum_a_i += curr_a_i
#     sum_a_a += curr_a_a

# print(f'AIF of module {class_name} is [{sum_a_i / sum_a_a}]')
