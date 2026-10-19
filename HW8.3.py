import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time

        print(f"{func.__name__} выполнился за {elapsed_time:.2f} сек.")
        return result

    return wrapper


@timer
def slow_test():
    time.sleep(1)
    return "OK"


print(slow_test())