
class PrimitiveParameter:
    """ Represents a parameter that is based on a simple Primitive Value """
    
    def __init__(self, field, optional=False, default=None):
        """ Initialize the Primitive Parameter with the field it should load the value from """
        self.field = field
        self.optional = optional
        self.defaultValue = default
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        if self.field in data:
            return data[self.field]
        elif self.optional:
            return self.defaultValue
        else:
            pass # Probably want to throw an exception