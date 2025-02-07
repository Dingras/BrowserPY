from PySide6.QtWidgets import QLineEdit, QPushButton, QComboBox, QWidget, QHBoxLayout
from PySide6.QtGui import QKeyEvent, QIcon
from PySide6.QtCore import Qt, Signal, QUrl
from assets.constants import suffixes
import re
from urllib.parse import urlparse

class SearchInput(QLineEdit):

    url_entered = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setPlaceholderText('Busca o ingresa una dirección URL')
        self.setAlignment(Qt.AlignLeft)
        self.editing = False
        self.show()

    def focusInEvent(self, event):
        self.editing = True
        super().focusInEvent(event)
        self.setCursorPosition(len(self.text()))  # Cursor al final al editar

    def focusOutEvent(self, event):
        self.editing = False
        super().focusOutEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        self.editing = True
        try:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                original_text = self.text().strip()
                search_engine = self.parent().search_selector.currentData()
                processed_url = self.process_input(original_text, search_engine)

                self.url_entered.emit(processed_url)
                self.editing = False
            
            super().keyPressEvent(event)

        except Exception as e:
            print(f"Error en entrada: {e}")

    def process_input(self, text : str, search_engine : str ) -> str:

        ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}(:\d+)?(/.*)?$'
        ipv6_pattern = r'^\[?([a-fA-F0-9:]+)\]?(?::\d+)?(/.*)?$'
        domain_pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/\S*)?$'

        is_valid_url = (
            text.startswith(('http://', 'https://')) or
            re.match(ip_pattern, text) or
            re.match(ipv6_pattern, text) or
            re.match(domain_pattern, text) or
            text.lower() == 'localhost'
        )

        if is_valid_url:
            return self.ensure_scheme(text)
        else:
            return self.build_search_url(text, search_engine)

    def ensure_scheme(self, url: str) -> str:
        if not url.startswith(('http://', 'https://')):
            return f'https://{url}'
        return url
    
    def build_search_url(self, query: str, engine: str) -> str:
        encoded_query = query.replace(' ', '+')
        return f'{engine}/search?q={encoded_query}'

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


class StarButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("assets/images/star.png")) # Ruta del ícono de estrella
        self.setText("")
        self.setFixedSize(32, 32)
        self.setIconSize(self.size())

        # Opcional: Estilo visual (redondeado)
        self.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 16px;
            }
        """)

class Navbar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)

        self.search_input = SearchInput(self)
        self.back_history_button = BackHistoryButton(self)
        self.forward_history_button = ForwardHistoryButton(self)
        self.search_selector = SearchSelector(self)
        self.favorite_button = StarButton(self)
        

        self.layout_h = QHBoxLayout()
        self.setLayout(self.layout_h)
        self.layout_h.addWidget(self.back_history_button)
        self.layout_h.addWidget(self.forward_history_button)
        self.layout_h.addWidget(self.search_selector)
        self.layout_h.addWidget(self.search_input)
        self.layout_h.addWidget(self.favorite_button)