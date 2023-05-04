

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
