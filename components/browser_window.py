from assets.constants import suffixes
from PySide6.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load("https://www.google.com")
        self.move(0, 50)
        self.setFixedHeight(670)
        self.setFixedWidth(1280)
        self.show()

    def load_url(self, url):
        try:
            self.setUrl(url)
        except Exception as e:
            print(e)
    
    def back_history(self):
        self.back()

    def forward_history(self):
        self.forward()
    