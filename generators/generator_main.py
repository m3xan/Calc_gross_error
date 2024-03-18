"""
generate Калькулятор.exe
"""

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '-n=Калькулятор',
    '-i=icon/calculator-Freepik.png',
    '-F',
    '-w',
    '--version-file=generators/properties.rc'
])
