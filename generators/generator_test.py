"""
generate Калькулятор_test.exe
"""

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '-n=Калькулятор_test',
    '-F'
])
