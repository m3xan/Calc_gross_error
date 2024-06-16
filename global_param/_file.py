"""
param collect other file path
"""
from abc import ABC
from typing import Final, final

type Path = str
type FileExist = str

class IterVar(ABC):
    def __iter__(self):
        for value in self.__dict__.values():
            yield value
@final
class FilePath(IterVar):
    def __init__(self) -> None:
        self.bd: Path = r'Data\Data_base'
        self.table_bd: Path = r'Data\Data_base\table.db'
        self.user_bd: Path =  r'Data\Data_base\users.db'
        self.documentation: Path = r'Документация\Докуметация пользовательская.docx'
        self.settings: Path =  r'Data\settings'
        self.json_setting: Path =  r'Data\settings\json'
        self.default_settings: Path =  r'Data\settings\json\default.json'
@final
class CriticalFilePath(IterVar):
    def __init__(self) -> None:
        self.bd: Path = r'Data\Data_base'
        self.user_bd: Path =  r'Data\Data_base\users.db'
        self.settings: Path =  r'Data\settings'

IMAGE_FILE_EXTENSIONS: Final[list[FileExist]] = ['.png', '.jpg', '.gif', '.svg']
