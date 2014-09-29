from factory import Factory

class DataSourceFactory(Factory):
    """ Represents a factory that acts as an entry point into some Data Source """
    
    def __init__(self, objectClass, parameters, dataSource, searchField):
        """ Initialize the Data Source Factory """
        Factory.__init__(self, objectClass, parameters)
        self.dataSource = dataSource
        self.searchField = searchField
        
    def load(self, key):
        """ Load the object from the given data """
        data = self.findData(key)
        if data is not None:
            return Factory.load(self, data)
        else:
            pass # Will want this to throw an exception
        return None
        
    def findData(self, key):
        """ Find the proper card JSON """
        matchingData = [data for data in self.dataSource.data if data[self.searchField] == key]
        if len(matchingData) > 0:
            return matchingData[0]
        return None