import time
from functools import wraps

def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                result = func(*args, **kwargs)

                if result == "PASSED":
                    return result

                print(f"Не успешно! попытка номер: {attempt}")

            print("Попыток больше нет")
            return "FAILURE"

        return wrapper
    return decorator


@retry(times=2)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"


print(flaky_test())