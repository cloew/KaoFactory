
class DataBoundFactory:
    """ Represents a Factory bound to a particular data source """
    
    def __init__(self, factory, source):
        """ Initialize the Data Bound Factory with the factory and the source """
        self.factory = factory
        self.source = source
        
    def load(self):
        """ Load and return the factory object from the data source """
        return self.factory.load(self.source.data)