import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout   
from PySide6.QtGui import QIcon    
from components.browser_window import BrowserWindow
from components.navbar import SearchInput, BackHistoryButton, ForwardHistoryButton, SearchSelector, Navbar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Configuración de la ventana inicial
        self.setWindowTitle("Browser.py")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon('assets/images/favicon.ico'))

        ## Componente general de la ventana
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        
        ## Barra de navegación
        self.navbar = Navbar(self)
        self.navbar.setFixedHeight(50)
        self.layout_principal.addWidget(self.navbar)
        
        ## Ventana del navegador
        self.browser_window = BrowserWindow(self)
        self.layout_principal.addWidget(self.browser_window)

        ## Conexiones
        self.browser_window.urlChanged.connect(self.update_url_bar)
        self.navbar.search_input.url_entered.connect(self.browser_window.load_url)
        self.navbar.back_history_button.clicked.connect(self.browser_window.back_history)
        self.navbar.forward_history_button.clicked.connect(self.browser_window.forward_history)

    def update_url_bar(self, url):
        if not self.navbar.search_input.hasFocus():
            self.navbar.search_input.blockSignals(True)
            self.navbar.search_input.setText(url.toString())
            self.navbar.search_input.setCursorPosition(0)
            self.navbar.search_input.blockSignals(False)

        if not self.navbar.search_input.editing:
            self.navbar.search_input.blockSignals(True)
            current_text = self.navbar.search_input.text()
        
        # Solo actualizar si es diferente
        if current_text != url.toString():
            self.navbar.search_input.setText(url.toString())
            self.navbar.search_input.setCursorPosition(0)
            
        self.navbar.search_input.blockSignals(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()