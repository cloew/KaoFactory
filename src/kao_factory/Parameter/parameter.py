from kao_factory.Exception.missing_parameter_exception import MissingParameterException

class Parameter:
    """ Represents a parameter """
    
    def __init__(self, optional=False, default=None):
        """ Initialize the Parameter """
        self.optional = optional
        self.defaultValue = default
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        if self.field in data:
            return self.__getvalue__(data)
        elif self.optional:
            return self.defaultValue
        else:
            raise MissingParameterException(self)
            
    def __repr__(self):
        """ Return the String Representation """
        return "{0} - {1}".format(self.__class__, self.field)