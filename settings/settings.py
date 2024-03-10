"""
Заглушка
"""

import os
import json
import functools
from  io import TextIOWrapper

from PySide6.QtCore import QFile, QTextStream

# переписать используя файловый дескриптор

def with_json(path, mode = 'r'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.exists(f'{path}\\{kwargs['id']}.json'):
                file_path = f'{path}\\{kwargs['id']}.json'
            else:
                file_path = f'{path}\\default.json'
            del kwargs['id']
            with open(file_path, mode, encoding= 'utf-8') as file:
                result = func(file, *args, **kwargs)
                return result
        return wrapper
    return decorator

@with_json(f'{os.getcwd()}\\Data\\settings\\json')
def load_json(file):
    """
    заглушка
    """
    return json.load(file)

def load_category_json(categor:str, user_id = None):
    return load_json(id= user_id)[categor]

def load_attribute(categor: str, attribute: str, user_id = None):
    return load_category_json(categor, user_id)[attribute]

@with_json(f'{os.getcwd()}\\Data\\settings\\json', 'w+')
def save_json(file: TextIOWrapper, data = None):
    """
    переделать
    """
    file.write(json.dumps(data, indent=4))

def save_data_json(categor: str, attribute: str | None, data: str, user_id = None):
    """
    заглушка
    """
    if attribute is None:
        # выполнять другую операцию, если атрибут не указан
        data_json = load_json(id=user_id)
        data_json[categor] = data
        save_json(data=data_json, id=user_id)
    else:
        # выполнять стандартную операцию, если атрибут указан
        data_json = load_json(id=user_id)
        data_json[categor][attribute] = data
        save_json(data=data_json, id=user_id)

def load_theme(self, user_id: str = None) -> str | None:
    """
    заглушка
    """
    theme = load_attribute('window', 'theme', user_id)
    canvas = load_attribute('window', 'canvas', user_id)
    qss_file_path = f"{os.getcwd()}/Data/settings/theme/{load_attribute('window', 'theme', user_id)}.qss"
    style_file = QFile(qss_file_path)
    if style_file.open(QFile.ReadOnly | QFile.Text):
        self.stream = QTextStream(style_file)
        self.setStyleSheet(self.stream.readAll())
        style_file.close()
        return theme, canvas
    print("Не удалось загрузить файл стилей")
    return None
