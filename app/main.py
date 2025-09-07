from typing import Callable


def cache(func: Callable) -> Callable:
    result: dict = {}

    def inner(*args) -> None:
        if args in result.keys():
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            function = func(*args)
            result[args] = function
            return function
    return inner
