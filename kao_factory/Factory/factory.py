from ..Exception.build_failed_exception import BuildFailedException
from future.utils import raise_with_traceback
import sys

class Factory:
    """ Represents a Factory to create objects of some class from data """
    
    def __init__(self, objectClass, *args, **kwargs):
        """ Initialize the Factory with the Object Class to create and the Factory Arguments used to populate the constructor """
        self.objectClass = objectClass
        self.args = args
        self.kwargs = kwargs
        
    def addArg(self, arg):
        """ Add the given arg. Useful for recursive Factories. """
        self.args.append(arg)
        
    def loadAll(self, dataList):
        """ Load the object from the given data """
        return [self.load(data) for data in dataList]
        
    def load(self, data):
        """ Load the object from the given data """
        try:
            args, kwargs = self.getArgs(data)
            return self.objectClass(*args, **kwargs)
        except Exception as e:
            raise_with_traceback(BuildFailedException(self, e))
            
    def getArgs(self, data):
        """ Return the arguments to call the constructor with """
        return self.getPositionalArgs(data), self.getKwargs(data)
        
    def getPositionalArgs(self, data):
        """ Return the positional arguments for this Factory and data """
        args = []
        missingArgs = []
        for arg in self.args:
            if not arg.isAvailable(data):
                missingArgs.append(arg)
            else:
                args.append(arg.getValue(data))
                
        if len(missingArgs) > 0:
            raise TypeError("{0} missing {1} required positional argument: {2}".format(self, len(missingArgs), ", ".join(["'{0}'".format(arg) for arg in missingArgs])))
            
        return args
        
    def getKwargs(self, data):
        """ Return the keyword arguments for this Factory and data """
        return {key:arg.getValue(data) for key, arg in self.kwargs.items() if arg.isAvailable(data)}
            
    def __repr__(self):
        """ Return the String representation of the factory """
        return "<{0} Factory>".format(self.objectClass)