"""
Заглушка
"""

import os
import re
import time

from generate_settings import write_customisation, add_resource

def generate_class_ui2py(path: str):
    """
    Заглушка
    """
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)

    for it in ui_list:
        file_path = os.path.join(path, it)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} -o {path}{os.sep}{file_name_without_extension}_class.py'
        os.popen(cmd)
        print('Успешная генерация файла')
        return f'{path}{os.sep}{file_name_without_extension}_class.py'

def generate_res_rc():
    """
    Переделать
    Заглушка
    """
    command = f'pyside6-rcc {os.getcwd()}\\icon\\res.qrc -o {os.getcwd()}\\window\\main_window\\res_rc.py'
    os.popen(command)
    print('Успешная генерация файла ресурсов')

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

def generate_about_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\about_window')
    time.sleep(1)
    add_resource(path)

def generate_add_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\add_window')
    time.sleep(1)
    add_resource(path)

def generate_setting_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\settings\\setting_window')
    time.sleep(1)
    add_resource(path)

def generate_load_window_class():
    """
    Заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\load_window')
    time.sleep(1)
    add_resource(path)

def generate_auto_save_window_class():
    """
    заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\settings\\auto_save_window')
    time.sleep(1)
    add_resource(path)

def generate_settings_window():
    """
    заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\settings\\main_settings')
    time.sleep(1)
    add_resource(path)

def generate_user_setting_window():
    """
    заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\settings\\user_setting')
    time.sleep(1)
    add_resource(path)

def generate_authorisation_window():
    """
    заглушка
    """
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\authorization_window')
    time.sleep(1)
    add_resource(path)

def a():
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\authorization_window\\internal_window\\login')
    time.sleep(1)
    add_resource(path)

def b():
    path = generate_class_ui2py(f'{os.getcwd()}\\window\\second_windows\\authorization_window\\internal_window\\registration')
    time.sleep(1)
    add_resource(path)

def genarate_all():
    """
    Заглушка
    """
    generate_main_window_class()
    generate_graph_window_class()
    generate_about_window_class()
    generate_add_window_class()
    generate_setting_window_class()
    generate_load_window_class()
    generate_auto_save_window_class()
    generate_settings_window()
    generate_user_setting_window()
    generate_authorisation_window()
    a()
    b()
    generate_res_rc()

if __name__ == '__main__':
    genarate_all()
