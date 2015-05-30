
class ErrorParameter:
    """ Represents a parameter that throws an exception when the value is retrieved """
        
    def getValue(self, data):
        """ Get the Primitive value from the data """
        raise Exception("Exception via Error Parameter")