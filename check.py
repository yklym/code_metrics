

from helpers import get_class_methods, is_method_inherited, is_method_overwritten, is_method_hidden, get_class_attributes


def check_inheritance_depth(target):
    parents = list(target.__bases__)

    if not len(parents):
        return 0  # not 1 because there always is a base class

    highest_depth = 0

    for parent in parents:
        curr_depth = check_inheritance_depth(parent)
        highest_depth = max(highest_depth, curr_depth)

    return highest_depth + 1


def get_children_number(target):
    return len(target.__subclasses__())


def get_all_children_number(_class):
    subclasses = set()
    work = [_class]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses


def get_class_mif_data(target):
    methods = get_class_methods(target)
    m_i = 0

    for method in methods:
        if is_method_inherited(target, method) and not is_method_overwritten(target, method):
            m_i += 1

    m_a = len(methods)

    return (m_i, m_a)


def get_mif(target):
    m_i, m_a = get_class_mif_data(target)

    return m_i / m_a


def get_class_mhf_data(target):
    methods = get_class_methods(target)
    m_h = 0
    m_v = 0

    for method in methods:
        if is_method_hidden(method):
            m_h += 1
        else:
            m_v += 1

    return (m_h, m_v)


def get_mhf(target):
    m_h, m_v = get_class_mhf_data(target)
    return m_h / (m_h + m_v)


def get_class_ahf_data(target):
    methods = get_class_attributes(target)
    m_h = 0
    m_v = 0

    for method in methods:
        if is_method_inherited(target, method):
            continue
        m_v += 1

        if is_method_hidden(method):
            m_h += 1

    return (m_h, m_v)


def get_ahf(target):
    a_h, a_d = get_class_ahf_data(target)
    return a_h / a_d


def get_class_aif_data(target):
    methods = get_class_attributes(target)
    a_i = 0

    for method in methods:
        if is_method_inherited(target, method) and not is_method_overwritten(target, method):
            a_i += 1

    a_a = len(methods)

    return (a_i, a_a)


def get_aif(target):
    a_i, a_a = get_class_aif_data(target)
    return a_i / a_a


def get_class_pof_data(target):
    methods = get_class_methods(target)
    m_o = 0
    m_n = 0

    for method in methods:
        if is_method_overwritten(target, method):
            m_o += 1
            # m_n += 1
        elif not is_method_inherited(target, method):
            m_n += 1

    return (m_o, m_n * max(len(get_all_children_number(target)), 1))


def get_pof(target):
    m_o, m_n = get_class_pof_data(target)
    # print('target', target.__name__, m_o, m_n)
    return m_o / max(m_n, 1)
