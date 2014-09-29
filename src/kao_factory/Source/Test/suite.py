import unittest

from kao_factory.Source.Test.json_source_test import suite as json_source_suite

suites = [json_source_suite]
suite = unittest.TestSuite(suites)