

class Rule:

    def __init__(self, **kwargs) -> None:
        self.attrs = kwargs

    def __repr__(self, classname: str) -> str:
        style = f'.{classname}' + '{'
        for attr, val in self.attrs.items():
            if attr == 'bg':
                style += f'background-color:{val};'
            elif attr == 'width':
                style += f'width:{val};'
            elif attr == 'height':
                style += f'height:{val};'
            elif attr == 'hlayout':
                style += f'align-items:{val};'
            elif attr == 'vlayout':
                style += f'justify-content:{val};'
            elif attr == 'padding':
                style += f'padding:{val};'
            elif attr == 'rounded':
                style += f'border-radius:{val};'
            elif attr == 'shadow':
                style += f'box-shadow:{val};'
            elif attr == 'size':
                style += f'font-size:{val};'
            elif attr == 'color':
                style += f'color:{val};'
            elif attr == 'weight':
                style += f'font-weight:{val};'
            elif attr == 'font':
                style += f'font-family:{val};'
            elif attr == 'style':
                style += f'text-decoration:{val};'
        
        style += '}'

        return style