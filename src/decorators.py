def add_method(object, method, name=None):
    """The following function will add any function to an instance in a cycle-free way by creating a specially modified class object and changing the instance’s class to it:"""
    if name is None: name = method.func_name
    class newclass(object._ _class_ _):
        pass
    setattr(newclass, name, method)
    object._ _class_ _ = newclass

def extends(cls):
    """Add method to class.
    Method should have at least one argument which will be used as reference to object (i.e. self).
    :param cls: Class to which method should be added
    :return:
    """

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator

def define_method(cls):
    """
    Decorator which adds a method to a class dynamically.
    
    Examples
    --------
    >>> class Foo:
    >>>     pass

    >>> @add_method(Foo)
    >>> def bar(self, parameter1):
            pass # Do something where self is a class instance
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        setattr(cls, func.__name__, wrapper)
        return func
    return decorator
