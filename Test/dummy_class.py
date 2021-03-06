from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

class DummyClass:
    """ Represents a dummy class for use in testing """
    
    def __init__(self, arg1, arg2, arg3):
        """ Initialize the dummy object """
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        
        
parameters = [PrimitiveParameter("arg1"), PrimitiveParameter("arg2"), PrimitiveParameter("arg3")]