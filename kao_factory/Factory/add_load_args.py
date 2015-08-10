from ..Args import FieldArg

def add_load_args(cls):
    """ Decorator to add the LoadArg and LoadAllArg methods to a Factory class """
    def LoadArg(self, name):
        return FieldArg(name, self.load)
    cls.LoadArg = LoadArg
        
    def LoadAllArg(self, name):
        return FieldArg(name, self.loadAll)
    cls.LoadAllArg = LoadAllArg
    return cls