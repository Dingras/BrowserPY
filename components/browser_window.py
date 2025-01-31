from assets.constants import suffixes
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load(QUrl("https://www.google.com"))
        self.show()

    def load_url(self, url):
        try:
            # Convertir a QUrl y validar
            qurl = QUrl(url)
            if not qurl.isValid():
                qurl = QUrl("https://" + url)
                
            self.load(qurl)
        except Exception as e:
            print(f"Error cargando URL: {e}")
    
    def back_history(self):
        self.back()

    def forward_history(self):
        self.forward()
    