import unittest

from kao_factory.Test.data_source_factory_test import suite as data_source_factory_suite
from kao_factory.Source.Test.suite import suite as source_suite

suites = [source_suite,
          data_source_factory_suite]
suite = unittest.TestSuite(suites)