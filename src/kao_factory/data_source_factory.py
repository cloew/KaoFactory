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
            return self.loadData(data)
        else:
            pass # Will want this to throw an exception
        return None
        
    def loadData(self, data):
        """ Load the given data """
        return Factory.load(self, data)
        
    def findData(self, key):
        """ Find the proper card JSON """
        matchingData = self.findMatchingData(key, self.searchField)
        if len(matchingData) > 0:
            return matchingData[0]
        return None
        
    def findMatchingData(self, key, field):
        """ Find the JSON data that matches the key """
        return [data for data in self.dataSource.data if data[field] == key]