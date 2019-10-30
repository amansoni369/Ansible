from ansible import errors
from ansible.errors import AnsibleParserError
import os, sys, yaml

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

class FilterModule(object):
    def filters(self):
        return {
            'upper_test': self.upper_test,
            'multiply_test': self.multiply_test
            }

    def upper_test(self, var):
        return var.upper()

    def multiply_test(self, val):
        return val*val
