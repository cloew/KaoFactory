import unittest

from kao_factory.factory import Factory
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from Test.dummy_class import DummyClass, parameters

class load(unittest.TestCase):
    """ Test cases of load """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.data = {"arg1":1, "arg2":2, "arg3":3}
        self.factory = Factory(DummyClass, parameters)
        
    def loaded(self):
        """ Test that the object can be loaded """
        object = self.factory.load(self.data)
        for key in self.data:
            self.assertEqual(getattr(object, key), self.data[key], "Each field on the object should match the value in the data")

# Collect all test cases in this class
testcasesLoad = ["loaded"]
suiteLoad = unittest.TestSuite(map(load, testcasesLoad))

##########################################################

class loadAll(unittest.TestCase):
    """ Test cases of loadAll """
    
    def  setUp(self):
        """ Build the Factory for the test """
        self.data = [{"arg1":1, "arg2":2, "arg3":3}, {"arg1":4, "arg2":5, "arg3":6}, {"arg1":7, "arg2":8, "arg3":9}]
        self.factory = Factory(DummyClass, parameters)
        
    def loaded(self):
        """ Test that the object can be loaded """
        objects = self.factory.loadAll(self.data)
        for object, data in zip(objects, self.data):
            for key in data:
                self.assertEqual(getattr(object, key), data[key], "Each field on the object should match the value in the data")

# Collect all test cases in this class
testcasesLoadAll = ["loaded"]
suiteLoadAll = unittest.TestSuite(map(loadAll, testcasesLoadAll))

##########################################################

# Collect all test cases in this file
suites = [suiteLoad, suiteLoadAll]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)