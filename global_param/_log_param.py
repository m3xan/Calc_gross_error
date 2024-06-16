"""
param for other logger settings
"""

from typing import Final

ECHO: Final = True

FORMAT: Final = '%(asctime)s %(levelname)s %(name)s %(message)s'

SQLLOGER: Final = 'sqlalchemy.engine.Engine'

LOG_PATH: Final = 'Data/logging'

START_LOGER: Final = f'{LOG_PATH}/start.log'
