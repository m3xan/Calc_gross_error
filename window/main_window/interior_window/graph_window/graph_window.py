from window.main_window.interior_window.graph_window.graph_window_class import Ui_GraphWindow, QMainWindow

class GraphWindow(QMainWindow):
    def __init__(self, user_id):
        super ().__init__()
        self.graph = Ui_GraphWindow()
        self.graph.setupUi(self, user_id)
