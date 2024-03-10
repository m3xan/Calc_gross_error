"""
generate Калькулятор.exe
"""
import os

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '-n=Калькулятор',
    f'-i={os.getcwd()}/icon/calculator-Freepik.png',
    '-F',
    '-w',
    f'--version-file={os.getcwd()}/generators/properties.rc'
])
