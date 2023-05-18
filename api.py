from check import check_inheritance_depth, get_class_aif_data, get_class_pof_data, get_children_number, get_class_mif_data, get_class_mhf_data, get_class_ahf_data

from inspect import getmembers, isclass


def get_module_inheritance_depth(module):
    module_classes = getmembers(module, isclass)
    max_depth_class = None
    max_depth = 0

    print('Test module depth--------------')

    for (_, _class) in module_classes:
        curr_depth = check_inheritance_depth(_class)
        if curr_depth > max_depth:
            max_depth = curr_depth

    print(
        f'max depth [{max_depth}] in module [{module.__name__}]')

    return max_depth, max_depth_class


def get_module_children_number(module):
    print('Test module children--------------')

    module_classes = getmembers(module, isclass)
    max_children_class = None
    max_children = 0

    for (class_name, _class) in module_classes:
        curr_depth = get_children_number(_class)
        if curr_depth > max_children:
            max_children = curr_depth
            max_children_class = class_name

    print(
        f'max children amount [{max_children}] in module [{module.__name__}] belongs to {max_children_class}')

    return max_children, max_children_class


def get_module_mif(module):
    print('Test MIF--------------')
    module_classes = getmembers(module, isclass)

    sum_m_i = 0
    sum_m_a = 0

    for (_, _class) in module_classes:
        curr_m_i, curr_m_a = get_class_mif_data(_class)
        sum_m_i += curr_m_i
        sum_m_a += curr_m_a

    print(
        f'MIF of module [{module.__name__}] is [{sum_m_i / max(sum_m_a, 1)}]')


def get_module_mhf(module):
    print('Test MHF--------------')

    module_classes = getmembers(module, isclass)

    sum_m_h = 0
    sum_m_v = 0

    for (_, _class) in module_classes:
        curr_m_h, curr_m_v = get_class_mhf_data(_class)
        sum_m_h += curr_m_h
        sum_m_v += curr_m_v

    print(
        f'MHF of module [{module.__name__}] is [{sum_m_h / max(sum_m_h + sum_m_v, 1)}]')


def get_module_ahf(module):
    print('Test AHF--------------')
    module_classes = getmembers(module, isclass)

    sum_a_h = 0
    sum_a_v = 0

    for (_, _class) in module_classes:
        curr_a_h, curr_a_v = get_class_ahf_data(_class)
        sum_a_h += curr_a_h
        sum_a_v += curr_a_v

    print(
        f'AHF of module [{module.__name__}] is [{sum_a_h / max(sum_a_v, 1)}]')


def get_module_aif(module):
    print('Test AIF--------------')
    module_classes = getmembers(module, isclass)

    sum_a_i = 0
    sum_a_a = 0

    for (_, _class) in module_classes:
        curr_a_i, curr_a_a = get_class_aif_data(_class)
        sum_a_i += curr_a_i
        sum_a_a += curr_a_a

    print(
        f'AIF of module [{module.__name__}] is [{sum_a_i / max(sum_a_a, 1)}]')


def get_module_pof(module):
    print('Test POF--------------')
    module_classes = getmembers(module, isclass)

    sum_m_o = 0
    sum_m_n_d_c = 0

    for (_, _class) in module_classes:
        curr_m_o, curr_m_n_d_c = get_class_pof_data(_class)
        sum_m_o += curr_m_o
        sum_m_n_d_c += curr_m_n_d_c

    print(
        f'POF of module [{module.__name__}] is [{sum_m_o / max(sum_m_n_d_c, 1)}]')
