from future.utils import raise_with_traceback
from kao_factory.Exception.build_failed_exception import BuildFailedException
from kao_factory.Exception.missing_parameter_exception import MissingParameterException

import sys

class FieldArg:
    """ Represents a Factory Argument that is based on a Field """
    
    def __init__(self, field, manipulator=None):
        """ Initialize the Arg with the field and an optional manipulator function to wrap the data """
        self.field = field
        self.manipulator = manipulator
        
    def isAvailable(self, data):
        """ Return if this Argument is available in the data """
        return self.field in data
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        argData = data[self.field]
        if self.manipulator is not None:
            argData = self.manipulator(argData)
        return argData
            
    def __repr__(self):
        """ Return the String Representation """
        return "<FieldArg({0})>".format(self.field)