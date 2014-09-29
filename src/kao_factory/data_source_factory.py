
class DataSourceFactory:
    """ Represents a factory that acts as an entry point into some Data Source """
    
    def __init__(self, dataSource, searchField):
        """ Initialize the Data Source Factory """
        self.dataSource = dataSource
        self.searchField = searchField
        
    def findData(self, key):
        """ Find the proper card JSON """
        matchingData = [data for data in self.dataSource.data if data[self.searchField] == key]
        if len(matchingData) > 0:
            return matchingData[0]
        return None