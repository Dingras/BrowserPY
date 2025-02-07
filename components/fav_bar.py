from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction
from functools import partial
import json
import os


class FavBar(QToolBar):
    def __init__(self, parent=None, load_url_callback = None):
        super().__init__(parent)
        self.setWindowTitle("Favoritos")
        self.json_file =  os.path.join(os.path.dirname(__file__), os.pardir, "assets", 'constants',"fav_web.json")
        self.load_url_callback = load_url_callback 
        self.load_favorites()
        self.show()

    def load_favorites(self):
        try:
            self.clear()
            with open(self.json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                favorites = data.get("favorites", [])
                if not isinstance(favorites, list):  # Asegurar que es una lista
                    raise ValueError("Formato inválido en 'favorites'")
                for site in favorites:
                    name = site.get("name", "Sin nombre")
                    url = site.get("url", "#")
                    action = QAction(name, self)
                    
                    # Conectar la acción con el método que cargará la URL
                    if self.load_url_callback:
                        action.triggered.connect(partial(self.load_url_callback, url))
                    
                    self.addAction(action)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.json_file}")
        except json.JSONDecodeError:
            print("Error decodificando JSON (archivo vacío o inválido)")
        except Exception as e:
            print(f"Error inesperado al cargar favoritos: {e}")
