
class PrimitiveParameter:
    """ Represents a parameter that is based on a simple Primitive Value """
    
    def __init__(self, field):
        """ Initialize the Primitive Parameter with the field it should load the value from """
        self.field = field
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        return data[self.field]