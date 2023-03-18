import os
from collections.abc import Callable

from src.views import View


class Py2html():

    def __init__(self, name) -> None:
        self.name = name
        self.views: dict[View] = dict()

    def add_view(self, path: str, func: Callable, *args) -> View:
        if not callable(func):
            raise Exception("view function passed not callable")
         
        self.views[path] = View(func, *args)
        return self.views[path]
    
    def compile(self) -> None:
        if not os.path.exists('./build/'):
            os.makedirs('./build/')
        
        if not os.path.exists('./build/assets/'):
            os.makedirs('./build/assets/')

        for path, view in self.views.items():
            view.compile(path)

