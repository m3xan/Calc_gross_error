"""
graph
==
Фабрика для рисования графика
version = 0.01
"""

from functions.graph.canvas import Canvas

class GraphicMaker:
    def empty_with_axes(self, color_fig, color_text):
        """
        Пустой график
        """
        return Canvas(color_fig= color_fig, color_text=color_text)
