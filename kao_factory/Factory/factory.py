from .arguments_helper import ArgumentsHelper
from ..Exception.build_failed_exception import BuildFailedException

from future.utils import raise_with_traceback
import sys

class Factory:
    """ Represents a Factory to create objects of some class from data """
    
    def __init__(self, objectClass, *args, **kwargs):
        """ Initialize the Factory with the Object Class to create and the Factory Arguments used to populate the constructor """
        self.objectClass = objectClass
        self.argsHelper = ArgumentsHelper(args, kwargs)
        
    def addArg(self, arg):
        """ Add the given arg. Useful for recursive Factories. """
        self.args.append(arg)
        
    def loadAll(self, dataList):
        """ Load the object from the given data """
        return [self.load(data) for data in dataList]
        
    def load(self, data):
        """ Load the object from the given data """
        try:
            args, kwargs = self.argsHelper.getArgs(data)
            return self.objectClass(*args, **kwargs)
        except TypeError as e:
            raise BuildFailedException(self, e)
            
    def __repr__(self):
        """ Return the String representation of the factory """
        return "<{0} Factory>".format(self.objectClass)