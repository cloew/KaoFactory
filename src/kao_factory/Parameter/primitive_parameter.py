from parameter import Parameter

class PrimitiveParameter(Parameter):
    """ Represents a parameter that is based on a simple Primitive Value """
    
    def __init__(self, field, optional=False, default=None):
        """ Initialize the Primitive Parameter with the field it should load the value from """
        self.field = field
        Parameter.__init__(self, optional=optional, default=default)
        
    def __getvalue__(self, data):
        """ Get the Primitive value from the data """
        return data[self.field]