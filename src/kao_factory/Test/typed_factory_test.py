import unittest

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from Test.dummy_class import DummyClass, parameters

class load(unittest.TestCase):
    """ Test cases of load """
    
    def  setUp(self):
        """ Build the Factories for the test """
        self.field = "type"
        self.existingType = "test"
        
        self.expectedValues = {"arg1":1, "arg2":2, "arg3":3}
        self.goodData = dict(self.expectedValues)
        self.goodData[self.field] = self.existingType
        
        self.factory = TypedFactory(self.field, {self.existingType:Factory(DummyClass, parameters)})
        
    def mappingExists(self):
        """ Test that the object is loaded properly when the type mapping exists """
        result = self.factory.load(self.goodData)
        self.assertIsNotNone(result, "The result should have been loaded")
        for key in self.expectedValues:
            self.assertEqual(getattr(result, key), self.goodData[key], "Each field on the result should match the value in the data")

# Collect all test cases in this class
testcasesLoad = ["mappingExists"]
suiteLoad = unittest.TestSuite(map(load, testcasesLoad))

##########################################################

# Collect all test cases in this file
suites = [suiteLoad]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)