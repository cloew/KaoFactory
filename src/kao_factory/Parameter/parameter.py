from future.utils import raise_with_traceback
from kao_factory.Exception.build_failed_exception import BuildFailedException
from kao_factory.Exception.missing_parameter_exception import MissingParameterException

import sys

class Parameter:
    """ Represents a parameter """
    
    def __init__(self, field, optional=False, default=None):
        """ Initialize the Parameter """
        self.field = field
        self.optional = optional
        self.defaultValue = default
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        if self.field in data:
            try:
                return self.__getvalue__(data)
            except Exception as e:
                raise_with_traceback(BuildFailedException(self, e))
        elif self.optional:
            return self.defaultValue
        else:
            raise MissingParameterException(self)
            
    def __repr__(self):
        """ Return the String Representation """
        return "<{0} - {1}>".format(self.__class__, self.field)