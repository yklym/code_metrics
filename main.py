from api import *
import unittest as test_module1
import bdb as test_module2
import cgi as test_module3


def main(module):

    if not module:
        return 1

    get_module_inheritance_depth(module)
    get_module_children_number(module)
    get_module_mif(module)
    get_module_mhf(module)
    get_module_ahf(module)
    get_module_aif(module)
    get_module_pof(module)


if (__name__ == '__main__'):
    main(test_module3)
    main(test_module2)
    main(test_module1)
