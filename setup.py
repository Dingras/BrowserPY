import sys
import os

from cx_Freeze import setup, Executable

files = ['assets','components','image']

exe = Executable(script='main.py', base='Win32GUI')

setup(
    name = "BrowserPy",
    version = '1.0',
    description = 'A simple web browser made in Python',
    author = 'Dingras',
    options = {
        'build_exe':{
            'include_files': files,
        }
    },
    executables = [exe]
)