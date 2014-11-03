from kao_factory.Exception.build_failed_exception import BuildFailedException
import sys

class Factory:
    """ Represents a Factory to create objects of some class from data """
    
    def __init__(self, objectClass, parameters):
        """ Initialize the Factory with the Object Class to create and the parameters to pass to the constructor """
        self.objectClass = objectClass
        self.parameters = parameters
        
    def loadAll(self, dataList):
        """ Load the object from the given data """
        return [self.load(data) for data in dataList]
        
    def load(self, data):
        """ Load the object from the given data """
        try:
            args = [parameter.getValue(data) for parameter in self.parameters]
            return self.objectClass(*args)
        except Exception as e:
            raise BuildFailedException("{0} Failed: {1}".format(self, e)), None, sys.exc_info()[2]
            
    def __repr__(self):
        """ Return the String representation of the factory """
        return "<Factory for {0}>".format(self.objectClass)