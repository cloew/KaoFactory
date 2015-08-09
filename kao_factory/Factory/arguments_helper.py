
class ArgumentsHelper:
    """ Helper class to deal with converting Factory Args to their values """
    
    def __init__(self, args, kwargs):
        """ Initialize with the args and kwargs """
        self.args = args
        self.kwargs = kwargs
            
    def getArgs(self, data):
        """ Return the arguments to call the constructor with """
        return self.getPositionalArgs(data), self.getKwargs(data)
        
    def getPositionalArgs(self, data):
        """ Return the positional arguments for this Factory and data """
        args = []
        missingArgs = []
        for arg in self.args:
            if not arg.isAvailable(data):
                missingArgs.append(arg)
            else:
                args.append(arg.getValue(data))
                
        if len(missingArgs) > 0:
            raise TypeError("{0} missing {1} required positional argument: {2}".format(data, len(missingArgs), ", ".join(["'{0}'".format(arg) for arg in missingArgs])))
            
        return args
        
    def getKwargs(self, data):
        """ Return the keyword arguments for this Factory and data """
        return {key:arg.getValue(data) for key, arg in self.kwargs.items() if arg.isAvailable(data)}