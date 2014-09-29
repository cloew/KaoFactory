import unittest

from kao_factory.Parameter.complex_parameter import ComplexParameter

class getValue(unittest.TestCase):
    """ Test cases of getValue """
    
    def  setUp(self):
        """ Build the Parameter for the test """
        self.field = "name"
        self.otherField = "Other Field"
        self.expectedValue = "Some Value"
        self.data = {self.field:self.expectedValue}
        
        self.parameter = ComplexParameter(self.field, self.helperMethod)
        self.optionalParameter = ComplexParameter(self.otherField, self.helperMethod, optional=True, default=self.expectedValue)
        
    def retrieved(self):
        """ Test that the value retrieved from the parameter is correct """
        value = self.parameter.getValue(self.data)
        self.assertEqual(value, self.expectedValue, "The Value should match the expected value")
        
    def optionalValue(self):
        """ Test that the value retrieved from the parameter is correct """
        value = self.optionalParameter.getValue(self.data)
        self.assertEqual(value, self.expectedValue, "The Value should match the expected value")
        
    def helperMethod(self, data):
        """ Helper Method to return the value for the Complex Parameter """
        return data

# Collect all test cases in this class
testcasesGetValue = ["retrieved", "optionalValue"]
suiteGetValue = unittest.TestSuite(map(getValue, testcasesGetValue))

##########################################################

# Collect all test cases in this file
suites = [suiteGetValue]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)