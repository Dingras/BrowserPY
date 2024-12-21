from PySide6.QtWidgets import QLineEdit, QPushButton, QComboBox
from PySide6.QtGui import QKeyEvent, QIcon
from PySide6.QtCore import Qt, Signal
from assets.constants import suffixes

class SearchInput(QLineEdit):

    url_entered = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setPlaceholderText('Busca o ingresa una direccion URL')
        self.move(165, 10)
        self.setFixedHeight(30)
        self.setFixedWidth(1110)
        self.show()

    def keyPressEvent(self, event: QKeyEvent):
        try:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                url = self.text().split()
                url = '+'.join(url)
                seeker = self.parent().search_selector.currentData()

                if not url.endswith(suffixes.valid_suffixes):
                    url = f'{seeker}/search?q={url}'

                if not url.startswith('http://') and not url.startswith('https://'):
                    url = f'https://www.{url}'

                self.url_entered.emit(url)
            else:
                super().keyPressEvent(event)
        except Exception as e:
            print(e)


class BackHistoryButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon('assets/images/back.png'))
        self.setFixedHeight(30)
        self.setFixedWidth(30)
        self.move(0, 10)
        self.show()

class ForwardHistoryButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon('assets/images/next.png'))
        self.setFixedHeight(30)
        self.setFixedWidth(30)
        self.move(30, 10)
        self.show()

class SearchSelector(QComboBox):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)
        self.setFixedWidth(100)
        self.move(60, 10)
        self.addItem(QIcon('assets/images/google.png'),'Google', 'https://www.google.com')
        self.addItem(QIcon('assets/images/bing.png'),'Bing', 'https://www.bing.com')
        self.addItem(QIcon('assets/images/yahoo.png'),'Yahoo', 'https://www.search.yahoo.com')
        self.show()
