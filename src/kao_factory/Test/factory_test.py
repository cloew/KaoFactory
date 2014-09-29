import unittest

from kao_factory.factory import Factory
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from Test.dummy_class import DummyClass

class load(unittest.TestCase):
    """ Test cases of load """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.parameters = [PrimitiveParameter("arg1"), PrimitiveParameter("arg2"), PrimitiveParameter("arg3")]
        self.data = {"arg1":1, "arg2":2, "arg3":3}
        self.factory = Factory(DummyClass, self.parameters)
        
    def loaded(self):
        """ Test that the object can be loaded """
        object = self.factory.load(self.data)
        for key in self.data:
            self.assertEqual(getattr(object, key), self.data[key], "Each field on the object should match the value in the data")

# Collect all test cases in this class
testcasesLoad = ["loaded"]
suiteLoad = unittest.TestSuite(map(load, testcasesLoad))

##########################################################

# Collect all test cases in this file
suites = [suiteLoad]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)