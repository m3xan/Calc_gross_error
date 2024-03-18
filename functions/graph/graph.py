"""
graph
==
Функция для рисования графика
version = 0.01
"""

from functions.graph.canvas import Canvas

def empty_graph(color_fig, color_text):
    """
    Пустой график
    """
    return Canvas(color_fig= color_fig, color_text=color_text)
