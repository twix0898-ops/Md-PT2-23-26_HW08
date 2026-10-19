import time
from functools import wraps


def wait_with_retry_until(timeout=10, interval=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            attempt = 1

            while time.time() - start_time < timeout:
                if func(*args, **kwargs):
                    print(f"Попытка {attempt}: успешно")
                    print("Элемент найден")
                    return True

                print(f"Попытка {attempt}: неуспешно")
                attempt += 1
                time.sleep(interval)

            print("Время ожидания истекло")
            return False

        return wrapper
    return decorator


@wait_with_retry_until(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # Имитация появления элемента


element_visible()