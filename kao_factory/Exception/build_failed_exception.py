
class BuildFailedException(Exception):
    """ Represents an exception for when a factory construction fails """
    
    def __init__(self, factory, exceptionToWrap):
        """ Initialize the excpetion with the factory and the exception that was thrown """
        Exception.__init__(self, "{0} Failed: {1}".format(factory, exceptionToWrap))