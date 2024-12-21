import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout   
from PySide6.QtGui import QIcon    
from components.browser_window import BrowserWindow
from components.navbar import SearchInput, BackHistoryButton, ForwardHistoryButton, SearchSelector, Navbar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Configuracion de la ventana inicial
        self.setWindowTitle("Browser.py")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon('assets/images/favicon.ico'))

        ## Componente general de la ventana
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        
        ## Barra de navegacion
        navbar = Navbar(self)
        navbar.setFixedHeight(50)
        self.layout_principal.addWidget(navbar)
        
        ## Ventana del navegador
        browser_window = BrowserWindow(self)
        self.layout_principal.addWidget(browser_window)

        ## Conexiones
        navbar.search_input.url_entered.connect(browser_window.load_url)
        navbar.back_history_button.clicked.connect(browser_window.back_history)
        navbar.forward_history_button.clicked.connect(browser_window.forward_history)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()