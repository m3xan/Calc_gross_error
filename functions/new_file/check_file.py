"""
заглушка
"""

import os
import logging
import concurrent.futures
from global_param import FILE_PATHS

def check_file(file_name: str) -> bool:
    """
    заглушка
    """
    file_exists = os.path.exists(file_name)
    logging.info('File %s %s', file_name, 'found' if file_exists else 'not found')
    return file_exists

def check_all_file() -> bool:
    """
    True когда все файлы для работы найдены.
    False когда какой либо файл не найден.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return all(executor.map(check_file, FILE_PATHS))
