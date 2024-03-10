def print_return(func):
    """
    принтит результат функции
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        object_type = "Метод" if hasattr(func, "__self__") else "Функция"
        object_name = func.__name__
        if object_type == "Метод":
            object_name = f'{object_name} класса {func.__self__.__class__.__name__}'
        print(f"{object_type} {object_name} завершился с результатом {result}")
        return result
    return wrapper
