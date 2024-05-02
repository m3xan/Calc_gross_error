"""
Заглушка
"""

import os
import json
from typing import overload
import logging

from PySide6.QtWidgets import QWidget

from global_param import SETTINGS_PATH

class JsonSettings:
    _instance = None
    __user_id = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id: int):
        if isinstance(user_id, int)  or user_id == 'option' or user_id == 'start':
            self.__user_id = user_id

    def load_json(self):
        """
        заглушка
        """
        with open(
            self.__check_user(),
            'r',
            encoding= 'utf-8'
        ) as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return None

    def save_json(self, data = None):
        """
        переделать
        """
        with open(
            self.__check_user(),
            'w+',
            encoding= 'utf-8'
        ) as file:
            file.write(json.dumps(data, indent= 2))

    def load_category_json(self, categor:str):
        """
        заглушка
        """
        return self.load_json()[categor]

    def load_attribute(self, categor: str, attribute: str):
        """
        заглушка
        """
        return self.load_category_json(categor)[attribute]

    @overload
    def save_data_json(self, categor: str, data: str) -> bool: ...
    @overload
    def save_data_json(self, categor: str, data: str, attribute: str) -> bool: ...

    def save_data_json(self, categor: str, data: str, attribute: str = None) -> bool:
        """
        заглушка
        """
        if attribute is None:
            # выполнять другую операцию, если атрибут не указан
            data_json = self.load_json()
            data_json[categor] = data
            self.save_json(data_json)
            return True
        # выполнять стандартную операцию, если атрибут указан
        data_json = self.load_json()
        data_json[categor][attribute] = data
        self.save_json(data_json)
        return True

    def save_start(self, name: str):
        self.__user_id = 'start'
        self.save_json(name)

    def load_theme(self, parent: QWidget) -> str | None:
        """
        заглушка
        """
        category = self.load_category_json('window')
        theme_name = category['theme']
        style_content = self.__load_data(theme_name)
        if style_content is not None:
            parent.setStyleSheet(style_content)

    def __load_data(self, theme_name):
        try:
            with open(
                f'Data/settings/theme/{theme_name}.qss',
                encoding= 'utf-8'
            ) as style_file:
                style_content = style_file.read()
                logging.info(f'load theme: {theme_name}')
                return style_content
        except FileNotFoundError:
            logging.warning('Не удалось найти файл стилей')
            return None

    def load_canvas(self) -> dict:
        """
        return theme canvas

        key:
        "text" color of the text,
        "canvas" color of the background
        """
        category = self.load_category_json('window')
        logging.info(f'canvas theme: {category['canvas']}')
        return category['canvas']

    def load_start(self):
        self.__user_id = 'start'
        return self.load_json()

    def __check_user(self) -> str:
        if os.path.exists(f'{SETTINGS_PATH}\\{self.__user_id}.json'):
            return f'{SETTINGS_PATH}\\{self.__user_id}.json'
        return f'{SETTINGS_PATH}\\default.json'
