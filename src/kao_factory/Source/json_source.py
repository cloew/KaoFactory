import json

class JsonSource:
    """ Represents a source of data from a json file """
    
    def __init__(self, filename):
        """ Initialize the JSON Source """
        self.filename = filename
        self.__json__ = None
            
    @property
    def data(self):
        """ Lazy-load the Json """
        if self.__json__ is None:
            self.loadJson()
        return self.__json__
        
    def loadJson(self):
        """ Load the JSON """
        with open(self.filename, 'r') as file:
            self.__json__ = json.load(file)