from typing import Callable


def cache(func: Callable) -> Callable:
    result: dict = {}
    def inner(*args) -> None:
        if args in result.keys():
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            result[args] = func(*args)
            return func(*args)
    return inner
