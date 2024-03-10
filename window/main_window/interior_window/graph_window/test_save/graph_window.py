from window.main_window.interior_window.graph_window.graph_window_class import Ui_GraphWindow, QMainWindow

class GraphWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super (GraphWindow, self).__init__()
        self.graph = Ui_GraphWindow()
        self.graph.setupUi(self)