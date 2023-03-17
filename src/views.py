from collections.abc import Callable

class View:

    def __init__(self, builder_func: Callable, *args) -> None:
        self.builder_func = builder_func
        self.buider_args = args

    def compile(self, path: str):
        with open(f'./build/{path}.html', 'w+') as f:
            f.write('<style> * { margin:0; padding:0; } </style>')
            f.write(repr(self.builder_func(*self.buider_args)))
