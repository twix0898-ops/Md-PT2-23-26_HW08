from functools import wraps

LOG_LEVEL = "DEBUG"

LEVELS = {
    "TRACE": 5,
    "DEBUG": 10,
    "INFO": 20,
    "NOTICE": 25,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,}


def conditional_log(min_level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if LEVELS[LOG_LEVEL] >= LEVELS[min_level]:
                print(f"[{LOG_LEVEL}] Запуск функции {func.__name__}")
                return func(*args, **kwargs)

            return None

        return wrapper
    return decorator


@conditional_log("DEBUG")
def debug_test():
    return "debug_result"


print(debug_test())