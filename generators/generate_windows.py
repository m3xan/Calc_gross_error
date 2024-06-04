"""
Заглушка
"""

import os
import re
import time
import subprocess
import threading
import concurrent
from concurrent.futures import ProcessPoolExecutor

from generate_settings import write_customisation, add_resource

WINDOW_PATH = [
    'window\\second_windows\\about_window',
    'window\\second_windows\\add_window',
    'window\\second_windows\\settings\\setting_window',
    'window\\second_windows\\load_window',
    'window\\second_windows\\settings\\auto_save_window',
    'window\\second_windows\\settings\\main_settings',
    'window\\second_windows\\settings\\user_setting',
    'window\\second_windows\\authorization_window',
    'window\\second_windows\\settings\\method_window',
    'window\\second_windows\\authorization_window\\internal_window\\login',
    'window\\second_windows\\authorization_window\\internal_window\\registration',
]

def generate_class_ui2py(path: str):
    """
    Заглушка
    """
    ui_file = find_ui_file(path)
    if ui_file is None:
        print('В директории файла нет')
    else:
        file_path: str = os.path.join(path, ui_file)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} -o {path}{os.sep}{file_name_without_extension}_class.py'
        try:
            subprocess.run(
                cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
            )
            print('Успешная генерация файла')
            return f'{path}{os.sep}{file_name_without_extension}_class.py'
        except subprocess.CalledProcessError as e:
            print('Ошибка при генерации файла')
            raise e
    return None

def find_ui_file(path: str):
    """Находит .ui файл в директории"""
    try:
        pattern = re.compile(r'.*\.ui')
        for file in os.listdir(path):
            if pattern.match(file):
                return file
        return None
    except FileNotFoundError:
        return None

def generate_res_rc():
    """
    Заглушка
    """
    command = 'pyside6-rcc icon\\res.qrc -o window\\main_window\\res_rc.py'
    try:
        subprocess.run(
            command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
        )
        print('Успешная генерация файла ресурсов')
    except subprocess.CalledProcessError as e:
        print('Ошибка при генерации файла ресурсов:')
        raise e

def generate_main_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py('window\\main_window')
    time.sleep(1)
    write_customisation(
        path,
        r'MainWindow.addDockWidget\(Qt.RightDockWidgetArea, self.dockWidget\)',
        "MainWindow.addDockWidget(JsonSettings().load_window().element.dockWidget, self.dockWidget)",
    )

def generate_graph_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py('window\\main_window\\interior_window\\graph_window')
    time.sleep(1)
    write_customisation(
        path,
        r'GraphWindow.addToolBar\(Qt.TopToolBarArea, self.toolBar\)',
        "GraphWindow.addToolBar(JsonSettings().load_window().element.toolBar, self.toolBar)"
    )

def generate_window(path: list):
    """делает файлики окон из директорий"""
    python_file_path =  generate_class_ui2py(path)
    if python_file_path is not None:
        time.sleep(1)
        add_resource(python_file_path)

def generate_window_wisout_changes(paths: list):
    """делает файлики окон из директорий"""
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(generate_window, path): path for path in paths}
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                raise e

def genarate_all():
    """
    Заглушка
    """
    threads = [
        threading.Thread(target=generate_main_window_class),
        threading.Thread(target=generate_graph_window_class),
        threading.Thread(target=generate_window_wisout_changes, args=(WINDOW_PATH,)),
        threading.Thread(target=generate_res_rc)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    genarate_all()
