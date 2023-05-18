import tests.mif.a as test_module

from api import get_module_mif

get_module_mif(test_module)

# from check import get_class_mif_data

# from inspect import getmembers, isclass

# print('Test MIF--------------')
# module_classes = getmembers(test_module, isclass)

# sum_m_i = 0
# sum_m_a = 0

# for (class_name, _class) in module_classes:
#     curr_m_i, curr_m_a = get_class_mif_data(_class)
#     sum_m_i += curr_m_i
#     sum_m_a += curr_m_a

# print(f'MIF of module {class_name} is [{sum_m_i / sum_m_a}]')
# print()
