"""
Заглушка
"""

import os
import re
import time
import subprocess

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
    'window\\second_windows\\authorization_window\\internal_window\\login',
    'window\\second_windows\\authorization_window\\internal_window\\registration'
]

def find_ui_file(path: str):
    """Находит .ui файл в директории"""
    files = os.listdir(path)
    pattern = re.compile(r'.*\.ui')
    for file in files:
        if pattern.match(file):
            return file
    return None

def generate_class_ui2py(path: str):
    """
    Заглушка
    """
    ui_file = find_ui_file(path)
    if ui_file is None:
        print('В директории файла нет')
    else:
        file_path: str = os.path.join(path, find_ui_file(path))
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

def generate_res_rc():
    """
    Переделать
    Заглушка
    """
    command = f'pyside6-rcc {os.getcwd()}\\icon\\res.qrc -o {os.getcwd()}\\window\\main_window\\res_rc.py'
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
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\main_window')
    time.sleep(1)
    write_customisation(path,
                  r'MainWindow.addDockWidget\(Qt.RightDockWidgetArea, self.dockWidget\)',
                  "MainWindow.addDockWidget(eval(load_attribute('window','dockWidget', user_name)), self.dockWidget)",
                  )
    time.sleep(1)
    write_customisation(path,
                  r'def setupUi\(self, MainWindow\):',
                  'def setupUi(self, MainWindow, user_name):',
                  )


def generate_graph_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\main_window\\interior_window\\graph_window')
    time.sleep(1)
    write_customisation(path,
                  r'GraphWindow.addToolBar\(Qt.TopToolBarArea, self.toolBar\)',
                  "GraphWindow.addToolBar(eval(load_attribute('window', 'toolBar', user_name)), self.toolBar)")
    write_customisation(path,
                  r'def setupUi\(self, GraphWindow\):',
                  'def setupUi(self, GraphWindow, user_name):',
                  )

def generate_window_wisout_change(paths: list):
    """делает файлики окон из директорий"""
    for path in paths:
        python_file_path =  generate_class_ui2py(path)
        if python_file_path is not None:
            time.sleep(1)
            add_resource(python_file_path)

def genarate_all():
    """
    Заглушка
    """
    generate_main_window_class()
    generate_graph_window_class()
    generate_window_wisout_change(WINDOW_PATH)
    generate_res_rc()

if __name__ == '__main__':
    genarate_all()
