import unittest

from kao_factory.Exception.build_failed_exception import BuildFailedException
from kao_factory.Exception.missing_parameter_exception import MissingParameterException
from kao_factory.Parameter.parameter import Parameter

class getValue(unittest.TestCase):
    """ Test cases of getValue """
    
    def setUp(self):
        """ Build the Parameter for the test """
        self.field = "name"
        self.otherField = "Other Field"
        self.expectedValue = "Some Value"
        self.data = {self.field:self.expectedValue}
        
        self.parameter = Parameter(self.field)
        self.parameter.__getvalue__ = self.getValue
        self.optionalParameter = Parameter(self.otherField, optional=True, default=self.expectedValue)
        
        self.calledInternalGetValue = False
        
    def internalGetValue_Valid(self):
        """ Test that the internal getvalue is called """
        value = self.parameter.getValue(self.data)
        self.assertTrue(self.calledInternalGetValue, "The internal get Value method should have been called")
        self.assertEqual(value, self.expectedValue, "The Value should match the expected value")
        
    def internalGetValue_ExceptionThrown(self):
        """ Test that the internal getvalue is called """
        self.parameter.__getvalue__ = self.getValue_RaiseException
        self.assertRaises(BuildFailedException, self.parameter.getValue, self.data)
        
    def fieldDoesNotExist(self):
        """ Test that the internal getvalue is called """
        self.assertRaises(MissingParameterException, self.parameter.getValue, {})
        
    def optionalValue(self):
        """ Test that the value retrieved from the parameter is correct """
        value = self.optionalParameter.getValue(self.data)
        self.assertEqual(value, self.expectedValue, "The Value should match the expected value")
        
    def getValue(self, data):
        """ Return the data """
        self.calledInternalGetValue = True
        return self.expectedValue
        
    def getValue_RaiseException(self, data):
        """ Return the data """
        self.calledInternalGetValue = True
        raise Exception("Test Exception")

# Collect all test cases in this class
testcasesGetValue = ["internalGetValue_Valid", "internalGetValue_ExceptionThrown", "fieldDoesNotExist", "optionalValue"]
suiteGetValue = unittest.TestSuite(map(getValue, testcasesGetValue))

##########################################################

# Collect all test cases in this file
suites = [suiteGetValue]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)