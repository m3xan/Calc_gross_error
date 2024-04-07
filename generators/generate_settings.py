"""
Заглушка
"""

import re
import functools
from io import TextIOWrapper

RES_IMPORT = r'from window.main_window import res_rc'
STANDART_RES_IMPORT = r'import res_rc'
ATREBUTE_IMPORT = r'from functions.settings.settings import JsonSettings'

def with_open(mode:str = 'r'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(args[0], mode, encoding='utf-8') as file:
                result = func(*args, **kwargs, file=file)
                return result
        return wrapper
    return decorator

@with_open('r+')
def write_customisation(path: str, original: str, changed: str, file: TextIOWrapper = None):
    data = file.read()
    data = re.sub(original, changed, data)
    if re.search(STANDART_RES_IMPORT, data):
        if not re.search(RES_IMPORT, data):
            data = re.sub(STANDART_RES_IMPORT, RES_IMPORT, data)
            # Преобразование текста в список строк
            lines = data.split('\n')

            # Поиск номера строки, содержащей подстроку
            found_line = next(
                (index + 2 for index, line in enumerate(lines) if RES_IMPORT in line),
                None
            )
    else:
        found_line = 21
    file.seek(0)
    file.write(data)
    if not re.search(ATREBUTE_IMPORT, data):
        str_ = f'{ATREBUTE_IMPORT}\n\n'
        file.seek(0)  # Переместить указатель файла в начало, чтобы вставить строку
        lines = file.readlines()
        lines.insert(found_line , str_)  # Вставить значение str_ в указанную строку
        file.seek(0)  # Перемещаем указатель файла обратно в начало
        file.writelines(lines)  # Перезаписываем файл со вставленной строкой

    print(f'Успешная генерация настроек {path}')


@with_open('r+')
def add_resource(path: str, file: TextIOWrapper = None):
    """
    Заглушка
    """
    data = file.read()
    data = re.sub(STANDART_RES_IMPORT, RES_IMPORT, data)
    file.seek(0)
    file.write(data)
