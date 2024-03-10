from functools import lru_cache

@lru_cache()
def check_password_strength(password):
    special_chars = "!@#$%^&*()-+"

    # Минимальная длина пароля
    if len(password) < 8:
        return False, "Пароль слишком короткий. Минимальная длина - 8 символов."

    # Проверка наличия цифр
    if not any(char.isdigit() for char in password):
        return False, "Пароль должен содержать хотя бы одну цифру."

    # Проверка наличия букв в верхнем регистре
    if not any(char.isupper() for char in password):
        return False, "Пароль должен содержать хотя бы одну букву в верхнем регистре."

    # Проверка наличия специальных символов
    if not any(char in special_chars for char in password):
        return False, "Пароль должен содержать хотя бы один специальный символ: !@#$%^&*()-+"

    return True, "Пароль надежный."
