from ..Exception.build_failed_exception import BuildFailedException
from future.utils import raise_with_traceback
import sys

class Factory:
    """ Represents a Factory to create objects of some class from data """
    
    def __init__(self, objectClass, parameters):
        """ Initialize the Factory with the Object Class to create and the parameters to pass to the constructor """
        self.objectClass = objectClass
        self.parameters = parameters
        
    def addParameter(self, parameter):
        """ Add the given parameter """
        self.parameters.append(parameter)
        
    def loadAll(self, dataList):
        """ Load the object from the given data """
        return [self.load(data) for data in dataList]
        
    def load(self, data):
        """ Load the object from the given data """
        try:
            args = [parameter.getValue(data) for parameter in self.parameters]
            return self.objectClass(*args)
        except Exception as e:
            raise_with_traceback(BuildFailedException(self, e))
            
    def __repr__(self):
        """ Return the String representation of the factory """
        return "<{0} Factory>".format(self.objectClass)