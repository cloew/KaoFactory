
class KeyDataBoundFactory:
    """ Represents a Factory bound to a particular data source that can access data by a key value """
    
    def __init__(self, factory, source, keyField):
        """ Initialize the Data Bound Factory with the factory and the source """
        self.factory = factory
        self.source = source
        self.keyField = keyField
        
    def loadAll(self):
        """ Load all items from the factory """
        return [self.loadData(data) for data in self.source.data]
        
    def load(self, key):
        """ Load and return the factory object from the data source """
        data = self.findData(key)
        if data is not None:
            try:
                return self.loadData(data)
            except Exception as e:
                raise_with_traceback(BuildFailedException("{0} load of {1}".format(self, key), e))
        else:
            raise KeyError(key)
        return None
        
    def loadData(self, data):
        """ Load the given data """
        return self.factory.load(data)
        
    def findData(self, key):
        """ Find the proper card JSON """
        matchingData = self.findMatchingData(key, self.keyField)
        if len(matchingData) > 0:
            return matchingData[0]
        return None
        
    def findMatchingData(self, key, field):
        """ Find the JSON data that matches the key """
        return [data for data in self.source.data if data[field] == key]