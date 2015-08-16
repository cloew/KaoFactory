
class StaticArg:
    """ Represents a Factory Argument that always returns the same value """
    
    def __init__(self, value):
        """ Initialize the Arg with the value to return """
        self.value = value
        
    def isAvailable(self, data):
        """ A Static Argument is always available """
        return True
        
    def getValue(self, data):
        """ Return the value """
        return self.value
            
    def __repr__(self):
        """ Return the String Representation """
        return "<StaticArg({0})>".format(self.value)