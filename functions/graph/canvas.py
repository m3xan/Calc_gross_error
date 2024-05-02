"""
заглушка
"""

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Canvas(FigureCanvasQTAgg):
    """
    заглушка
    """
    def __init__(self, color_fig: str, color_text: str):
        self.fig = Figure(facecolor = color_fig)
        self.ax = self.fig.add_subplot()
        self.update_collor(color_fig, color_text)
        super().__init__(self.fig)

    def update_collor(self, color_fig: str, color_text: str):
        self.fig.set_facecolor(color_fig)
        self.ax.set_title('График распределения', color= color_text)
        self.ax.set_xlabel('Величина', color= color_text)
        self.ax.set_ylabel('Количество', color= color_text)
        self.ax.tick_params(labelcolor= color_text)
        self.ax.set()
        self.ax.grid(True)
        self.ax.set_facecolor(color_fig)
