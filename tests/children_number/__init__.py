from .a import *
import tests.children_number.a as test_module
from api import get_module_children_number


get_module_children_number(test_module)

# from inspect import getmembers, isclass
# module_classes = getmembers(test_module, isclass)
# max_children_class = None
# max_children = 0

# for (class_name, _class) in module_classes:
#     curr_depth = get_children_number(_class)
#     if curr_depth > max_children:
#         max_children = curr_depth
#         max_children_class = class_name

# print(
#     f'max children amount [{max_children}] in module belongs to {max_children_class}')
