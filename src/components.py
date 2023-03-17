from abc import ABC, abstractclassmethod

class Component(ABC):

    def __init__(self, *args, **kwargs) -> None:
        self.components = args
        self.attrs = kwargs

    @abstractclassmethod
    def __repr__(self) -> str:
        pass

    @abstractclassmethod
    def get_style(self) -> str:
        pass

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
        for key, val in self.attrs.items():
            if key == 'bg':
                style += f'background-color:{val};'
            elif key == 'width':
                style += f'width:{val};'
            elif key == 'height':
                style += f'height:{val};'
            elif key == 'hlayout':
                style += f'justify-content:{val};'
            elif key == 'vlayout':
                style += f'align-items:{val};'
            elif key == 'padding':
                style += f'padding:{val};'
            elif key == 'rounded':
                style += f'border-radius:{val}'
        
        style += '"'
        return style

class Vstack(Layout):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<div{self.get_style()}>{super().__repr__()}</div>'
    
    def get_style(self) -> str:
        style = ' style="display:flex; flex-direction:column;'
        for key, val in self.attrs.items():
            if key == 'bg':
                style += f'background-color:{val};'
            elif key == 'width':
                style += f'width:{val};'
            elif key == 'height':
                style += f'height:{val};'
            elif key == 'hlayout':
                style += f'align-items:{val};'
            elif key == 'vlayout':
                style += f'justify-content:{val};'
            elif key == 'padding':
                style += f'padding:{val};'
            elif key == 'rounded':
                style += f'border-radius:{val}'
        
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
        for key, val in self.attrs.items():
            if key == 'size':
                style += f'font-size:{val};'
            elif key == 'color':
                style += f'color:{val};'
            elif key == 'padding':
                style += f'padding:{val};'
        
        style += '"'
        return style

''' Interaction components '''
class Interaction(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def __repr__(self) -> str:
        return f'{"".join([repr(comp) for comp in self.components])}'


class Link(Interaction):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        href = ' href="' + self.attrs.get('href') + '" ' if self.attrs.get('href') else ''
        return f'<a{href}{self.get_style()}>{super().__repr__()}</a>'
    
    def get_style(self) -> str:
        style = ' style="'
        for key, val in self.attrs.items():
            if key == 'style':
                style += f'text-decoration:{val};'
            elif key == 'color':
                style += f'color:{val};'
            elif key == 'padding':
                style += f'padding:{val};'
        
        style += '"'
        return style

class Button(Interaction):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')


class Input(Interaction):
    
    def __init__(self, type, placeholder='Input', **kwargs) -> None:
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
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')