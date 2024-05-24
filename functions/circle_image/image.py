
from typing import overload
import re
import os

from global_param import STANDART_IMAGE, FILE_EXTENSIONS

class Image:
    standart_image = STANDART_IMAGE

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, image_path: str) -> None: ...

    def __init__(self, image_path = None) -> None:
        self.set_image_path(image_path)

    def set_image_path(self, image_path: str) -> bool:
        if self.__check_path(image_path):
            self.__image = image_path
            return True
        self.__image = self.standart_image
        return False

    def get_image_path(self) -> str:
        return self.__image

    @staticmethod
    def __check_path(image_path):
        if image_path:
            if all((
                os.path.isfile(image_path),
                os.path.splitext(image_path)[1] in FILE_EXTENSIONS
            )):
                return True
        return False

    def isfullpath(self):
        if os.path.abspath(self.__image):
            return True
        return False

    def __str__(self) -> str:
        return self.get_image_path()
    def __len__(self):
        return len(re.findall(r'[\\]|/', self.__image))
