
def check_password_strength(password):

    # Минимальная длина пароля
    if len(password) < 8:
        return False, 'Пароль слишком короткий. Минимальная длина - 8 символов.'

    # Проверка наличия цифр
    if not any(char.isdigit() for char in password):
        return False, 'Пароль должен содержать хотя бы одну цифру.'

    # Проверка наличия букв в верхнем регистре
    if not any(char.isupper() for char in password):
        return False, 'Пароль должен содержать хотя бы одну букву в верхнем регистре.'

    # Проверка наличия специальных символов
    if not any(char in '!@#$%^&*()-+' for char in password):
        return False, 'Пароль должен содержать хотя бы один специальный символ: !@#$%^&*()-+'

    return True, 'Пароль надежный.'
