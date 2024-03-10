"""
заглушка
"""

import os

def check_file(file_name: str) -> bool:
    """
    заглушка
    """
    file_exists = os.path.exists(file_name)
    print(f'Файл {file_name} {"найден" if file_exists else "не найден"}')
    return file_exists

def check_all_file() -> bool:
    """
    True когда все файлы для работы найдены.
    False когда какой либо файл не найден.
    """
    file_paths = [
        r'Data\Data_base',
        r'Документация\Докуметация пользовательская.docx',
        r'Data\settings\json\default.json'
    ]
    return all(check_file(path) for path in file_paths)
