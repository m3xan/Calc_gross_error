"""
заглушка
"""

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Canvas(FigureCanvasQTAgg):
    """
    заглушка
    """
    def __init__(self, color_fig, color_text):
        self.fig = Figure(facecolor = color_fig)
        self.ax = self.fig.add_subplot()
        self.ax.tick_params(labelcolor= color_text)
        self.ax.set_title('названия у ничего', color= color_text)
        self.ax.set_xlabel('ничего по x', color= color_text)
        self.ax.set_ylabel('ничего по y', color= color_text)
        self.ax.tick_params(labelcolor= color_text)
        self.ax.set()
        self.ax.grid(True)
        self.ax.set_facecolor(color_fig)
        super().__init__(self.fig)

    def update_collor(self, color_fig, color_text):
        self.fig.set_facecolor(color_fig)
        self.ax.set_title('названия у ничего', color= color_text)
        self.ax.set_xlabel('ничего по x', color= color_text)
        self.ax.set_ylabel('ничего по y', color= color_text)
        self.ax.tick_params(labelcolor= color_text)
        self.ax.set()
        self.ax.grid(True)
        self.ax.set_facecolor(color_fig)
        # self.draw()