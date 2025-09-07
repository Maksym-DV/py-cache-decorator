from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result: dict = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs)))
        if key in result:
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            function = func(*args)
            result[args] = function
            return function
    return inner
