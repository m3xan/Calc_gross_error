import os

def action_help_click():
    try:
        os.startfile(f"{os.getcwd()}\Документация\Докуметация пользовательская.docx")
        return True
    except FileNotFoundError as err:
        raise err
