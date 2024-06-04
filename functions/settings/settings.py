"""
Заглушка
"""

import os
import json
import logging
from typing import Self

from PySide6.QtWidgets import QWidget

from global_param import SETTINGS_PATH

from .pydantic_model import Calculation, UserSettings, CanvasModel, Window, AutoSave

class JsonSettings:
    """for json format"""
    _instance = None
    __user_id = None

    def __new__(cls) -> Self:
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def get_user_id(self) -> None:
        return self.__user_id

    def set_user_id(self, user_id: int):
        if isinstance(user_id, int):
            self.__user_id = user_id

    def load_json(self) -> UserSettings | None:
        """
        заглушка
        """
        try:
            with open(
                self.__check_user()[1],
                encoding= 'utf-8'
            ) as file:
                return UserSettings.model_validate(
                    json.load(file)
                )
        except json.decoder.JSONDecodeError as err:
            logging.error(f'file wasn`t read, error: {err}', exc_info= True)
            return None
        except Exception as err:
            logging.critical(err, exc_info= True)
            raise err

    def save_json(self, data: UserSettings):
        """
        переделать
        """
        try:
            isdefaul, path = self.__check_user()
            if isdefaul:
                return
            with open(path, 'w+', encoding= 'utf-8') as file:
                file.write(
                    data.model_dump_json(indent= 2, exclude_none= True)
                )
        except json.decoder.JSONDecodeError as err:
            logging.warning(err, exc_info= True)
        except Exception as err:
            logging.critical(err, exc_info= True)
            raise err

    def load_window(self) -> Window | None:
        """
        заглушка
        """
        if settings := self.load_json():
            return settings.window
        return None

    def load_auto_save(self) -> AutoSave | None:
        """
        заглушка
        """
        if settings := self.load_json():
            return settings.auto_save
        return None

    def load_calculation(self) -> Calculation | None:
        """
        заглушка
        """
        if settings := self.load_json():
            return settings.calculation
        return None

    def load_canvas(self) -> CanvasModel | None:
        """
        return theme canvas

        key:
        "text" color of the text,
        "canvas" color of the background
        """
        if settings := self.load_json():
            logging.info(f'canvas theme: {settings.window.canvas}')
            return settings.window.canvas
        return None

    def save_start(self, name: str) -> None:
        """
        save name in start file
        """
        u_id = self.__user_id
        self.__user_id = 'start'
        try:
            isdefaul, path = self.__check_user()
            if isdefaul:
                return
            with open(path, 'w+', encoding= 'utf-8') as file:
                file.write(
                    json.dumps(name)
                )
        except Exception as err:
            logging.critical(err, exc_info=True)
            raise err
        finally:
            self.__user_id = u_id

    def load_theme(self, parent: QWidget) -> str | None:
        """
        заглушка
        """
        user_settings = self.load_json()
        style_content = self.__load_data(
            user_settings.window.theme
        )
        if style_content is not None:
            parent.setStyleSheet(style_content)

    def __load_data(self, theme_name) -> str | None:
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

    def load_start(self) -> str | None:
        """
        load start name 
        if swith True on last user
        """
        _u_id = self.__user_id
        try:
            self.__user_id = 'start'
            isdefaul, path = self.__check_user()
            if isdefaul:
                return
            with open(path, encoding= 'utf-8') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return None
        except Exception as err:
            logging.critical(err, exc_info=True)
            raise err
        finally:
            self.__user_id =_u_id

    def raw_json_loads(self) -> str | None:
        """
        load row data json with out validation
        """
        _u_id = self.__user_id
        try:
            self.__user_id = 'option'
            isdefaul, path = self.__check_user()
            if isdefaul:
                return
            with open(path, 'r', encoding= 'utf-8'
            ) as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return None
        except Exception as err:
            logging.critical(err, exc_info=True)
            raise err
        finally:
            self.__user_id =_u_id

    def __check_user(self) -> tuple[bool, str]:
        if os.path.exists(f'{SETTINGS_PATH}\\{self.__user_id}.json'):
            return False, f'{SETTINGS_PATH}\\{self.__user_id}.json'
        return True, f'{SETTINGS_PATH}\\default.json'
