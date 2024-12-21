from PySide6.QtWidgets import QLineEdit, QPushButton, QComboBox, QWidget, QHBoxLayout
from PySide6.QtGui import QKeyEvent, QIcon
from PySide6.QtCore import Qt, Signal
from assets.constants import suffixes

class SearchInput(QLineEdit):

    url_entered = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setPlaceholderText('Busca o ingresa una direccion URL')
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
        self.show()

class ForwardHistoryButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon('assets/images/next.png'))
        self.show()

class SearchSelector(QComboBox):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.addItem(QIcon('assets/images/google.png'),'Google', 'https://www.google.com')
        self.addItem(QIcon('assets/images/bing.png'),'Bing', 'https://www.bing.com')
        self.addItem(QIcon('assets/images/yahoo.png'),'Yahoo', 'https://www.search.yahoo.com')
        self.show()


class Navbar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.search_input = SearchInput(self)
        self.back_history_button = BackHistoryButton(self)
        self.forward_history_button = ForwardHistoryButton(self)
        self.search_selector = SearchSelector(self)
        

        self.layout_h = QHBoxLayout()
        self.setLayout(self.layout_h)
        self.layout_h.addWidget(self.back_history_button)
        self.layout_h.addWidget(self.forward_history_button)
        self.layout_h.addWidget(self.search_selector)
        self.layout_h.addWidget(self.search_input)