from abc import ABC


class Action(ABC):

    def __init__(self, **kwargs) -> None:
        self.attrs = kwargs

    
    def __repr__(self) -> str:
        style = ''
        for attr, val in self.attrs.items():
            if attr == 'bg':
                style += f'background-color:{val} !important;'
            elif attr == 'width':
                style += f'width:{val} !important;'
            elif attr == 'height':
                style += f'height:{val} !important;'
            elif attr == 'hlayout':
                style += f'align-items:{val} !important;'
            elif attr == 'vlayout':
                style += f'justify-content:{val} !important;'
            elif attr == 'padding':
                style += f'padding:{val} !important;'
            elif attr == 'rounded':
                style += f'border-radius:{val} !important;'
            elif attr == 'shadow':
                style += f'box-shadow:{val} !important;'
            elif attr == 'size':
                style += f'font-size:{val} !important;'
            elif attr == 'color':
                style += f'color:{val} !important;'
            elif attr == 'weight':
                style += f'font-weight:{val} !important;'
            elif attr == 'font':
                style += f'font-family:{val} !important;'
            elif attr == 'style':
                style += f'text-decoration:{val} !important;'
            elif attr == 'transform':
                style += f'transform:{val} !important;'
        return style


class Hover(Action):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __repr__(self, classname: str) -> str:
        return f'.{classname}:hover' + '{' + super().__repr__() + '}'
