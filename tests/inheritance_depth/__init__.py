import tests.inheritance_depth.a as test_module
from api import get_module_inheritance_depth

# from check import check_inheritance_depth

# from inspect import getmembers, isclass

# module_classes = getmembers(test_module, isclass)
# max_depth_class = None
# max_depth = 0

# for (class_name, _class) in module_classes:
#     curr_depth = check_inheritance_depth(_class)
#     if curr_depth > max_depth:
#         max_depth = curr_depth
#         max_depth_class = class_name

get_module_inheritance_depth(test_module)
