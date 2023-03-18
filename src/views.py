from collections.abc import Callable

from src.actions import Action

class View:

    def __init__(self, builder_func: Callable, *args) -> None:
        self.builder_func = builder_func
        self.buider_args = args
        self.actions: list[tuple[str, Action]] = list()

    def add_action(self, action: Action, classname: str) -> None:
        self.actions.append((classname, action))

    def compile(self, path: str) -> None:
        with open(f'./build/{path}.html', 'w+') as f:
            f.write('<!DOCTYPE html>')
            f.write('<html lang="en">')
            f.write('<head>')
            f.write('<meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0">')
            f.write('<title>Document</title>')
            f.write('<style> * { margin:0; padding:0; box-sizing: border-box;}')
            for classname, action in self.actions:
                f.write(action.__repr__(classname))
            f.write(f'</style>')
            f.write('</head>')
            f.write('<body>')
            f.write(repr(self.builder_func(*self.buider_args)))
            f.write('</body>')
            f.write('</html>')
