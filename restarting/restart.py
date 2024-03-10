"""
Заглушка
"""

import os
import sys

def restart_program():
    """
    Заглушка
    """
    print('Происходит перезапуск приложения\n')
    python = sys.executable
    os.execl(python, python, *sys.argv)
