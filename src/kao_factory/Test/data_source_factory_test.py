import unittest

from kao_factory.data_source_factory import DataSourceFactory
from Test.dummy_data_source import DummyDataSource

class findData(unittest.TestCase):
    """ Test cases of findData """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.field = "name"
        self.existingName = "Test"
        self.nonExistingName = "Blah"
        self.expectedResult = {self.field:self.existingName}
        source = DummyDataSource([self.expectedResult])
        self.factory = DataSourceFactory(source, self.field)
        
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
suites = [suiteFindData]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)