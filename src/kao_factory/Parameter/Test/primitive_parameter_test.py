import unittest

from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

class getValue(unittest.TestCase):
    """ Test cases of getValue """
    
    def  setUp(self):
        """ Build the Parameter for the test """
        self.field = "name"
        self.expectedValue = "Some Value"
        self.data = {self.field:self.expectedValue}
        self.parameter = PrimitiveParameter(self.field)
        
    def retrieved(self):
        """ Test that the value retrieved from the parameter is correct """
        value = self.parameter.getValue(self.data)
        self.assertEqual(value, self.expectedValue, "The Value should match the expected value")

# Collect all test cases in this class
testcasesGetValue = ["retrieved"]
suiteGetValue = unittest.TestSuite(map(getValue, testcasesGetValue))

##########################################################

# Collect all test cases in this file
suites = [suiteGetValue]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)