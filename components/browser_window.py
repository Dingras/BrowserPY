import json
import os
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
    
    def save_favorite_url(self, name, url):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            json_path = os.path.join(parent_dir, "assets", "constants", "fav_web.json")
            
            data = {"favorites": []}
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = {"favorites": []}
            
            if 'favorites' not in data:
                data['favorites'] = []
            
            # Evitar duplicados
            if any(fav['url'] == url for fav in data['favorites']):
                print("Esta URL ya está en favoritos")
                return
                
            data['favorites'].append({"name": name, "url": url})
            
            with open(json_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                
        except Exception as e:
            print(f"Error guardando favorito: {e}")