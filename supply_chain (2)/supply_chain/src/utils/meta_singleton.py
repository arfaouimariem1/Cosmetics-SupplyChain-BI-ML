"""meta_singleton module"""


class MetaSingleton(type):
    """
    Creates singleton for any class
    Use it by marking the target class with `metaclass=MetaSingleton`
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
