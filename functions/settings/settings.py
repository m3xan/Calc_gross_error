"""
Заглушка
"""

import os
import json
import functools
from  io import TextIOWrapper
import logging

def with_json(path, mode = 'r'):
    """
    заглушка
    """
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

@with_json('Data\\settings\\json')
def load_json(file):
    """
    заглушка
    """
    return json.load(file)

def load_category_json(categor:str, user_id = None):
    """
    заглушка
    """
    return load_json(id= user_id)[categor]

def load_attribute(categor: str, attribute: str, user_id = None):
    """
    заглушка
    """
    return load_category_json(categor, user_id)[attribute]

@with_json('Data\\settings\\json', 'w+')
def save_json(file: TextIOWrapper, data = None):
    """
    переделать
    """
    file.write(json.dumps(data, indent= 2))

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
    category = load_category_json('window', user_id)
    theme_name = category['theme']
    try:
        with open(
            f'Data/settings/theme/{theme_name}.qss',
            encoding= 'utf-8'
        ) as style_file:
            style_content = style_file.read()
            self.setStyleSheet(style_content)
            logging.info('load theme: %s %s', theme_name, category['canvas'])
            return theme_name, category['canvas']
    except FileNotFoundError:
        logging.warning('Не удалось найти файл стилей')
        return None
