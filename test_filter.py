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
        try:
            return var.upper()
        except Exception as ex:
            display.vvv("unexpected error occured %s")

    def multiply_test(self, val):
        errors = self.__divide_test(val)
        if errors:
            return({
                'warning': 'cant divide by 0'
            })
        else:
            return val/2

    def __divide_test(self, val):
        errors = []
        try:
            result = val/2
        except:
            display.vvv('cant divide by 0')
            return({
                'errors': 'cant divide by 0'
            })
        return errors
