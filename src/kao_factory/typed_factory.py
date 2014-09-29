
class TypedFactory:
    """ Represents a Factory to build differently depending on the value of a field in the data """
    
    def __init__(self, field, valueToFactory):
        """ Initialize the Typed Factory with the field to check and the factory each value corresponds to """
        self.field = field
        self.valueToFactory = valueToFactory
        
    def addFactory(self, value, factory):
        """ Add the factory to the mapping """
        self.valueToFactory[value] = factory
        
    def loadAll(self, dataList):
        """ Load the object from the given data """
        return [self.load(data) for data in dataList]
        
    def load(self, data):
        """ Load from the given data """
        value = data[self.field]
        factory = self.valueToFactory[value]
        return factory.load(data)