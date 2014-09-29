
class ComplexParameter:
    """ Represents a parameter that is based on a complex process or object """
    
    def __init__(self, field, method):
        """ Initialize the Complex Parameter with the field and method to consturct the complex value """
        self.field = field
        self.method = method
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        return self.method(data[self.field])