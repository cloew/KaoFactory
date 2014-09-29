import unittest

from kao_factory.Parameter.Test.primitive_parameter_test import suite as primitive_parameter_suite

suites = [primitive_parameter_suite]
suite = unittest.TestSuite(suites)