
class Factory:
    """ Represents a Factory to create objects of some class from data """
    
    def __init__(self, objectClass, parameters):
        """ Initialize the Factory with the Object Class to create and the parameters to pass to the constructor """
        self.objectClass = objectClass
        self.parameters = parameters
        
    def load(self, data):
        """ Load the object from the given data """
        args = [parameter.getValue(data) for parameter in self.parameters]
        return self.objectClass(*args)