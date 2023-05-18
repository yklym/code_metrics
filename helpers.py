def get_class_methods(target):
    method_list = [func for func in dir(
        target) if callable(getattr(target, func)) and not func.startswith("__")]
    return method_list


def get_class_attributes(target):
    attr_list = [func for func in dir(
        target) if not callable(getattr(target, func)) and not func.startswith("__")]
    return attr_list


def get_method_origin(_class, method):
    if method not in _class.__dict__:  # Not defined in _class : inherited
        return 1
    # elif hasattr(super(_class), method):  # Present in parent : overloaded
    #     print('2')

    #     return 2
    elif len(_class.__bases__) and any(hasattr(x, method) for x in _class.__bases__):
        return 2
    else:  # Not present in parent : newly defined

        return 0


def is_method_inherited(_class, method):
    return get_method_origin(_class, method) == 1


def is_method_overwritten(_class, method):
    # print("get_method_origin(_class, method)",
    #       get_method_origin(_class, method))
    return get_method_origin(_class, method) == 2


def is_method_original(_class, method):
    return get_method_origin(_class, method) == 0


def is_method_hidden(method):
    return method.startswith('_')
