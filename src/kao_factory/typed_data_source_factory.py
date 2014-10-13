from data_source_factory import DataSourceFactory
from typed_factory import TypedFactory

class TypedDataSourceFactory(DataSourceFactory):
    """ Represents a factory that acts as an entry point into some Data Source """
    
    def __init__(self, field, valueToFactory, dataSource, searchField):
        """ Initialize the Data Source Factory """
        DataSourceFactory.__init__(self, None, [], dataSource, searchField)
        self.typedFactory = TypedFactory(field, valueToFactory)
        
    def loadData(self, data):
        """ Load the given data """
        return self.typedFactory.load(data)