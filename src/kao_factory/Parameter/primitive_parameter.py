from .parameter import Parameter

class PrimitiveParameter(Parameter):
    """ Represents a parameter that is based on a simple Primitive Value """
        
    def __getvalue__(self, data):
        """ Get the Primitive value from the data """
        return data[self.field]