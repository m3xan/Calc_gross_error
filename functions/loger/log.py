import logging
import os

def start_loger():
    """init loger"""
    try:
        if not os.path.isdir(r'Data\logging'):
            os.mkdir(r'Data\logging')

        logging.basicConfig(
            filename='Data/logging/start.log',
            level=logging.CRITICAL,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding= 'utf-8'
        )

        logging.getLogger('sqlalchemy.engine.Engine').propagate = False
        return True
    except Exception as err:
        raise err

def change_loger(user_id: str, level: int):
    """change loger for user loger"""
    if level == 10:
        logging.getLogger('sqlalchemy.engine.Engine').propagate = True

    logging.getLogger().setLevel(level)

    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    new_file_handler = logging.FileHandler(
        f'Data/logging/{user_id}.log',
        encoding= 'utf-8'
    )
    new_file_handler.setLevel(logging.DEBUG)
    new_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    root.addHandler(new_file_handler)
