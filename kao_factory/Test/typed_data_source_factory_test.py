import unittest

from kao_factory.factory import Factory
from kao_factory.typed_data_source_factory import TypedDataSourceFactory
from Test.dummy_class import DummyClass, parameters
from Test.dummy_data_source import DummyDataSource

class loadData(unittest.TestCase):
    """ Test cases of loadData """
    
    def  setUp(self):
        """ Build the Factories for the test """
        self.typeField = "type"
        self.searchField = "name"
        self.existingType = "test"
        
        self.expectedValues = {"arg1":1, "arg2":2, "arg3":3}
        self.goodData = dict(self.expectedValues)
        self.goodData[self.typeField] = self.existingType
        
        source = DummyDataSource([self.goodData])
        self.factory = TypedDataSourceFactory(self.typeField, {self.existingType:Factory(DummyClass, parameters)}, source, self.searchField)
        
    def mappingExists(self):
        """ Test that the object is loaded properly when the type mapping exists """
        result = self.factory.loadData(self.goodData)
        self.assertIsNotNone(result, "The result should have been loaded")
        for key in self.expectedValues:
            self.assertEqual(getattr(result, key), self.goodData[key], "Each field on the result should match the value in the data")

# Collect all test cases in this class
testcasesLoadData = ["mappingExists"]
suiteLoadData = unittest.TestSuite(map(loadData, testcasesLoadData))

##########################################################

# Collect all test cases in this file
suites = [suiteLoadData]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)