from functools import wraps


def validate_params(expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for name, expected_type in expected_types.items():
                if name in kwargs and not isinstance(kwargs[name], expected_type):
                    raise TypeError(f"{name} должен быть {expected_type.__name__}")

            return func(*args, **kwargs)

        return wrapper
    return decorator


@validate_params({"username": str, "age": int})
def create_user(**kwargs):
    return f"Пользователь {kwargs['username']} создан"


print(create_user(username="test", age=25))

try:
    print(create_user(username="test", age="25"))
except TypeError as error:
    print(error)