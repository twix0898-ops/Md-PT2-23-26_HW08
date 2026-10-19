import time
from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n


print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(6))
print(expensive_calculation(5))


def count_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Выполняю {func.__name__} с аргументом {args[0]}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Время выполнения: {elapsed}")
        return result

    return wrapper


@count_exec_time
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n


print(expensive_calculation(5))