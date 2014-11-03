import unittest

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.Exception.build_failed_exception import BuildFailedException
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from Test.dummy_class import DummyClass, parameters
from Test.dummy_data_source import DummyDataSource
from Test.error_parameter import ErrorParameter

class load(unittest.TestCase):
    """ Test cases of load """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.field = "name"
        self.existingName = "Test"
        self.nonExistingName = "Blah"
        
        self.expectedValues = {"arg1":1, "arg2":2, "arg3":3}
        self.data = dict(self.expectedValues)
        self.data[self.field] = self.existingName
        
        source = DummyDataSource([self.data])
        self.factory = DataSourceFactory(DummyClass, parameters, source, self.field)
        self.errorFactory = DataSourceFactory(DummyClass, [ErrorParameter()], source, self.field)
        
    def dataFound(self):
        """ Test that the data can be properly found """
        result = self.factory.load(self.existingName)
        self.assertIsNotNone(result, "The result should have been found and loaded")
        for key in self.expectedValues:
            self.assertEqual(getattr(result, key), self.data[key], "Each field on the result should match the value in the data")
        
    def dataFound_ErrorLoading(self):
        """ Test that the data can be properly found """
        self.assertRaises(BuildFailedException, self.errorFactory.load, self.existingName)
        
    def dataNotFound(self):
        """ Test that the data can be properly found """
        result = self.factory.load(self.nonExistingName)
        self.assertIsNone(result, "The result should not have been found or loaded")

# Collect all test cases in this class
testcasesLoad = ["dataFound", "dataFound_ErrorLoading", "dataNotFound"]
suiteLoad = unittest.TestSuite(map(load, testcasesLoad))

##########################################################

class findData(unittest.TestCase):
    """ Test cases of findData """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.field = "name"
        self.existingName = "Test"
        self.nonExistingName = "Blah"
        self.expectedResult = {self.field:self.existingName}
        source = DummyDataSource([self.expectedResult])
        self.factory = DataSourceFactory(DummyClass, parameters, source, self.field)
        
    def dataFound(self):
        """ Test that the data can be properly found """
        result = self.factory.findData(self.existingName)
        self.assertIsNotNone(result, "The result should have been found")
        self.assertEqual(result, self.expectedResult, "The result should have matched the expected value")
        
    def dataNotFound(self):
        """ Test that the data can be properly found """
        result = self.factory.findData(self.nonExistingName)
        self.assertIsNone(result, "The result should not have been found")

# Collect all test cases in this class
testcasesFindData = ["dataFound", "dataNotFound"]
suiteFindData = unittest.TestSuite(map(findData, testcasesFindData))

##########################################################

# Collect all test cases in this file
suites = [suiteLoad, suiteFindData]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)