
class BuildFailedException(Exception):
    """ Represents an exception for when a factory construction fails """
    
    def __init__(self, objectThatFailedToBuild, exceptionToWrap):
        """ Initialize the excpetion with the object that failed to build and the exception that was thrown """
        Exception.__init__(self, "{0} Failed: {1}".format(objectThatFailedToBuild, exceptionToWrap))