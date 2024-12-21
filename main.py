import sys
from PySide6.QtWidgets import QApplication, QMainWindow   
from PySide6.QtGui import QIcon    
from components.browser_window import BrowserWindow
from components.navbar import SearchInput, BackHistoryButton, ForwardHistoryButton, SearchSelector


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.back_history_button = BackHistoryButton(self)
        self.forward_history_button = ForwardHistoryButton(self)
        self.search_selector = SearchSelector(self)
        self.search_input = SearchInput(self)

        self.browser_window = BrowserWindow(self)

        self.search_input.url_entered.connect(self.browser_window.load_url)
        self.back_history_button.clicked.connect(self.browser_window.back_history)
        self.forward_history_button.clicked.connect(self.browser_window.forward_history)

        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon('assets/images/favicon.ico'))
        self.setWindowTitle('Browser.Py')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()