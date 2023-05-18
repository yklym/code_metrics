import tests.mhf.a as test_module
from api import get_module_mhf

get_module_mhf(test_module)
# from check import get_class_mif_data, get_class_mhf_data

# from inspect import getmembers, isclass

# print('Test MHF--------------')
# module_classes = getmembers(test_module, isclass)

# sum_m_h = 0
# sum_m_v = 0

# for (class_name, _class) in module_classes:
#     curr_m_h, curr_m_v = get_class_mhf_data(_class)
#     sum_m_h += curr_m_h
#     sum_m_v += curr_m_v

# print(f'MHF of module {class_name} is [{sum_m_h / (sum_m_h + sum_m_v)}]')
# print()
