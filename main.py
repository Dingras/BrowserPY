import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout 
from PySide6.QtWidgets import QInputDialog, QLineEdit  
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWebEngineCore import QWebEngineProfile
from components.browser_window import BrowserWindow
from PySide6.QtWebEngineCore import QWebEngineSettings
from components.fav_bar import FavBar
from components.navbar import Navbar

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

        ## Ventana del navegador (Creación de objeto)
        self.browser_window = BrowserWindow(self)
        
        ## Ventana del nevegador (Configuración)
        settings = self.browser_window.settings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        settings.setAttribute(QWebEngineSettings.WebGLEnabled, True)
        settings.setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
        
        ## Manejo de eventos de pantalla completa
        self.browser_window.page().fullScreenRequested.connect(self.handle_fullscreen)
        
        ## Barra de favoritos
        self.favbar = FavBar(self,load_url_callback=self.browser_window.load_url)
        self.layout_principal.addWidget(self.favbar)
        
        ## Barra de navegación
        self.navbar = Navbar(self)
        self.layout_principal.addWidget(self.navbar)
        
        ## Ventana del navegador (Colocación en Widget)
        self.layout_principal.addWidget(self.browser_window)

        ## Conexiones
        self.browser_window.urlChanged.connect(self.update_url_bar)
        self.navbar.search_input.url_entered.connect(self.browser_window.load_url)
        self.navbar.back_history_button.clicked.connect(self.browser_window.back_history)
        self.navbar.forward_history_button.clicked.connect(self.browser_window.forward_history)
        self.navbar.favorite_button.clicked.connect(self.handle_save_favorite)

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
    
    def handle_save_favorite(self):
        current_url = self.browser_window.url().toString()
        name, ok = QInputDialog.getText(
            self, 
            "Guardar Favorito", 
            "Nombre del sitio:", 
            QLineEdit.Normal, 
            ""
        )
        if ok and name:
            self.browser_window.save_favorite_url(name, current_url)
            self.favbar.load_favorites()

    def handle_fullscreen(self, request):
        request.accept()
        if request.toggleOn():
            self.browser_window.setWindowFlags(Qt.Window)
            self.browser_window.showFullScreen()
        else:
            self.browser_window.setWindowFlags(Qt.Widget)
            self.browser_window.showNormal()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()