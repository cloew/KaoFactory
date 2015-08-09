import unittest

from kao_factory.Parameter.Test.parameter_test import suite as parameter_suite
from kao_factory.Parameter.Test.complex_parameter_test import suite as complex_parameter_suite
from kao_factory.Parameter.Test.primitive_parameter_test import suite as primitive_parameter_suite

suites = [primitive_parameter_suite,
          complex_parameter_suite,
          parameter_suite]
suite = unittest.TestSuite(suites)