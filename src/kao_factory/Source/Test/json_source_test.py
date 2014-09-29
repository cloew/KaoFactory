import unittest

from kao_factory.Source.json_source import JsonSource

JSON_FILENAME = 'resources/test_data.json'
EXPECTED_NAME = 'Test'

class data(unittest.TestCase):
    """ Test cases of data """
    
    def  setUp(self):
        """ Build the JSON Source for the test """
        self.source = JsonSource(JSON_FILENAME)
        
    def dataLoaded(self):
        """ Test that the data is loaded once accessed """
        data = self.source.data
        self.assertEqual(len(data), 1, "There should be a single entry")
        self.assertEqual(data[0]["name"], EXPECTED_NAME, "The name should be the expected value")

# Collect all test cases in this class
testcasesData = ["dataLoaded"]
suiteData = unittest.TestSuite(map(data, testcasesData))

##########################################################

# Collect all test cases in this file
suites = [suiteData]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)