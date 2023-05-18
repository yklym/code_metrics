import tests.pof.a as test_module

from api import get_module_pof
get_module_pof(test_module)


# from inspect import getmembers, isclass
# from check import get_class_mif_data, get_class_mhf_data
# print('Test POF--------------')
# module_classes = getmembers(test_module, isclass)

# sum_m_o = 0
# sum_m_n_d_c = 0

# for (class_name, _class) in module_classes:
#     curr_m_o, curr_m_n_d_c = get_class_mhf_data(_class)
#     sum_m_o += curr_m_o
#     sum_m_n_d_c += curr_m_n_d_c

# print(f'POF of module {class_name} is [{sum_m_o / (sum_m_n_d_c)}]')
