from parameter import Parameter

class ComplexParameter(Parameter):
    """ Represents a parameter that is based on a complex process or object """
    
    def __init__(self, field, method, optional=False, default=None):
        """ Initialize the Complex Parameter with the field and method to consturct the complex value """
        self.field = field
        self.method = method
        Parameter.__init__(self, optional=optional, default=default)
        
    def __getvalue__(self, data):
        """ Get the Primitive value from the data """
        return self.method(data[self.field])