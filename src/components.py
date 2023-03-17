from abc import ABC, abstractclassmethod
from PIL import Image as Im
import PIL

class Component(ABC):

    def __init__(self, *args, **kwargs) -> None:
        self.components = args
        self.attrs = kwargs


''' Layout components '''
class Layout(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'{"".join([repr(comp) for comp in self.components])}'
        #return f'<div{style}>{"".join([repr(comp) for comp in self.components])}</div>'


class Hstack(Layout):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<div{self.get_style()}>{super().__repr__()}</div>'
        #return super().__repr__(self.get_style())
    
    def get_style(self) -> str:
        style = ' style="display: flex;'
        for attr, val in self.attrs.items():
            if attr == 'bg':
                style += f'background-color:{val};'
            elif attr == 'width':
                style += f'width:{val};'
            elif attr == 'height':
                style += f'height:{val};'
            elif attr == 'hlayout':
                style += f'justify-content:{val};'
            elif attr == 'vlayout':
                style += f'align-items:{val};'
            elif attr == 'padding':
                style += f'padding:{val};'
            elif attr == 'rounded':
                style += f'border-radius:{val}'
            elif attr == 'shadow':
                style += f'box-shadow:{val};'
        
        style += '"'
        return style

class Vstack(Layout):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<div{self.get_style()}>{super().__repr__()}</div>'
    
    def get_style(self) -> str:
        style = ' style="display:flex; flex-direction:column;'
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
        
        style += '"'
        return style
    

class Spacing(Layout):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')


''' Text components '''
class Text(Component):
    
    def __init__(self, text, **kwargs) -> None:
        super().__init__(**kwargs)
        self.text = text

    def __repr__(self) -> str:
        return f'<p{self.get_style()}>{self.text}</p>'

    def get_style(self) -> str:
        style = ' style="'
        for attr, val in self.attrs.items():
            if attr == 'size':
                style += f'font-size:{val};'
            elif attr == 'color':
                style += f'color:{val};'
            elif attr == 'padding':
                style += f'padding:{val};'
            elif attr == 'weight':
                style += f'font-weight:{val}'
            elif attr == 'font':
                style += f'font-family:{val}'
        
        style += '"'
        return style

''' Interaction components '''
class Interaction(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'{"".join([repr(comp) for comp in self.components])}'


class Link(Interaction):
    
    def __init__(self, link: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.link = link
        self.text = self.attrs.get('text')

    def __repr__(self) -> str:
        href = ' href="' + self.link + '"'
        if self.text:
            return f'<a{href}{self.get_style()}>{self.text}</a>' 
        return f'<a{href}{self.get_style()}>{super().__repr__()}</a>'
    
    def get_style(self) -> str:
        style = ' style="'
        for attr, val in self.attrs.items():
            if attr == 'style':
                style += f'text-decoration:{val};'
            elif attr == 'color':
                style += f'color:{val};'
            elif attr == 'padding':
                style += f'padding:{val};'
            elif self.text:
                if attr == 'size':
                    style += f'font-size:{val};'
                elif attr == 'color':
                    style += f'color:{val};'
                elif attr == 'weight':
                    style += f'font-weight:{val}'
                elif attr == 'font':
                    style += f'font-family:{val}'
        
        style += '"'
        return style

class Button(Interaction):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<div{self.get_style()}>{super().__repr__()}</div>'

    def get_style(self) -> str:
        style = ' style="display:flex;align-items:center;justify-content:center;'
        for attr, val in self.attrs.items():
            if attr == 'bg':
                style += f'background-color:{val};'
            elif attr == 'width':
                style += f'width:{val};'
            elif attr == 'height':
                style += f'height:{val};'
            elif attr == 'padding':
                style += f'padding:{val};'
            elif attr == 'rounded':
                style += f'border-radius:{val};'
            elif attr == 'shadow':
                style += f'box-shadow:{val};'
        
        style += '"'
        return style


class Input(Interaction):
    
    def __init__(self, type: str, placeholder='Input', **kwargs) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.placeholder = placeholder

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')


''' Media components '''
class Media(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')


class Image(Media):
    
    def __init__(self, path: str, alt='Image', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.path = path
        self.alt = alt

    def __repr__(self) -> str:
        self.save_asset()
        return f'<img src="{self.path}" alt="{self.alt}"{self.get_style()}>'
    
    def get_style(self) -> str:
        style = ' style="display:flex;align-items:center;justify-content:center;'
        for attr, val in self.attrs.items():
            if attr == 'width':
                style += f'width:{val};'
            elif attr == 'height':
                style += f'height:{val};'
            elif attr == 'rounded':
                style += f'border-radius:{val};'
            elif attr == 'shadow':
                style += f'box-shadow:{val};'
        
        style += '"'
        return style
    
    def save_asset(self) -> None:
        img = Im.open(self.path)
        name = self.path.split('/')[-1]
        self.path = f'assets/{name}'
        img.save(f'./build/{self.path}')