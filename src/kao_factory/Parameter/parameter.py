
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
            pass # Probably want to throw an exception