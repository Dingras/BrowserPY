# BrowserPY

![BrowserPY Screenshot](https://github.com/Dingras/BrowserPY/blob/main/image/image.png?raw=true)

BrowserPY es un navegador web simple hecho en Python usando PySide6.

## Características

- Navegación básica
- Seleccion de motores de busquedas
- Interfaz de usuario simple y limpia

## Requisitos

- Python 3.x
- PySide6

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Dingras/BrowserPY.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd BrowserPY
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv .venv
    ```
4. Activa el entorno:
    ```bash
    .venv/Scripts/activate
    ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Ejecuta el navegador con el siguiente comando:
```bash
python main.py
```

## Crear un Ejecutable

Si deseas crear un ejecutable, sigue estos pasos después de instalar las dependencias:

1. Ejecuta el archivo setup.py:
```bash
python setup.py build
```
2. Se creará un directorio `build` que contendrá todos los archivos necesarios para ejecutar la aplicación.

3. Dentro del directorio `build`, encontrarás el archivo `main.exe` (o su equivalente para tu sistema). Haz doble clic en él para iniciar BrowserPY.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.