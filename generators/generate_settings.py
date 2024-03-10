"""
Заглушка
"""

import re
import functools
from io import TextIOWrapper

# переписать используя файловый дескриптор

RES_IMPORT = 'from window.main_window import res_rc'

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
    if re.search(r'import res_rc', data):
        if not re.search(RES_IMPORT, data):
            data = re.sub(r'import res_rc', RES_IMPORT, data)
            # Преобразование текста в список строк
            lines = data.split('\n')

            # Поиск номера строки, содержащей подстроку
            found_line = next(
                (index + 2 for index, line in enumerate(lines) if "from window.main_window import res_rc" in line),
                None
            )
    else:
        found_line = 21
    file.seek(0)
    file.write(data)
    if not re.search(r'from settings.settings import load_attribute', data):
        str_ = 'from settings.settings import load_attribute\n\n'
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
    data = re.sub(r'import res_rc', 'from window.main_window import res_rc', data)
    file.seek(0)
    file.write(data)
