from functools import wraps


def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user != required_role:
                raise PermissionError(
                    f"Требуется роль {required_role}, текущая: {user}"
                )
            return func(user, *args, **kwargs)

        return wrapper
    return decorator

user_one = "user"
user_two = "admin"

@require_role("admin")
def admin_test(*args):
    print("Выполняется админский тест")
    return "Success"

try:
    admin_test(user_one)
except PermissionError as error:
    print(f"Ошибка: {error}")