from typing import Callable


def cache(func: Callable) -> Callable:
    result: list = []
    def inner(*args, **kwargs) -> None:
        if func(*args, **kwargs) in result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result.append(func(*args, **kwargs))
    return inner
