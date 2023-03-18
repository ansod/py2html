from PIL import Image as Im

class Component:

    def __init__(self, *args, **kwargs) -> None:
        self.components = args
        self.attrs = kwargs
        self.classname = kwargs.get('classname')
        if self.classname:
            kwargs.pop('classname')

    def get_classname(self) -> str:
        if not self.classname:
            return ''
        
        return self.classname
    
    @staticmethod
    def name() -> str:
        return 'py2htmlComponent'

    @staticmethod
    def base_type() -> str:
        return 'Component'


''' Layout components '''
class Layout(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'{"".join([repr(comp) for comp in self.components])}'
    
    def get_classname(self) -> str:
        return super().get_classname()
    
    @staticmethod
    def name() -> str:
        return 'py2htmlLayout'
    


class Hstack(Layout):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:   
        return f'<div class="py2htmlHstack {super().get_classname()}"{self.get_style()}>{super().__repr__()}</div>'
    
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
    
    @staticmethod
    def name() -> str:
        return 'py2htmlHstack'


class Vstack(Layout):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str: 
        return f'<div class="py2htmlVstack {super().get_classname()}"{self.get_style()}>{super().__repr__()}</div>'
    
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
    
    @staticmethod
    def name() -> str:
        return 'py2htmlVstack'



''' Text components '''
class Text(Component):
    
    def __init__(self, text, **kwargs) -> None:
        super().__init__(**kwargs)
        self.text = text

    def __repr__(self) -> str:
        return f'<p class="py2htmlText {super().get_classname()}"{self.get_style()}>{self.text}</p>'

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
                style += f'font-weight:{val};'
            elif attr == 'font':
                style += f'font-family:{val};'
            elif attr == 'align':
                style += f'text-align:{val};'
        
        style += '"'
        return style
    
    @staticmethod
    def name() -> str:
        return 'py2htmlText'


''' Interactive components '''
class Interactive(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'{"".join([repr(comp) for comp in self.components])}'
    
    def get_classname(self) -> str:
        return super().get_classname()
    
    @staticmethod
    def name() -> str:
        return 'py2htmlInteractive'


class Link(Interactive):
    
    def __init__(self, link: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.link = link
        self.text = self.attrs.get('text')

    def __repr__(self) -> str:
        href = ' href="' + self.link + '"'
        return f'<a class="py2htmlLink {super().get_classname()}"{href}{self.get_style()}>{self.text if self.text else super().__repr__()}</a>'
    
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
                    style += f'font-weight:{val};'
                elif attr == 'font':
                    style += f'font-family:{val};'
                elif attr == 'align':
                    style += f'text-align:{val};'
        
        style += '"'
        return style
    
    @staticmethod
    def name() -> str:
        return 'py2htmlLink'
    

class Button(Interactive):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<div class="py2htmlButton {super().get_classname()}"{self.get_style()}>{super().__repr__()}</div>'

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
    
    @staticmethod
    def name() -> str:
        return 'py2htmlButton'


class Input(Interactive):
    
    def __init__(self, type: str, placeholder='Input', **kwargs) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.placeholder = placeholder

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')
    
    @staticmethod
    def name() -> str:
        return 'py2htmlInput'


''' Media components '''
class Media(Component):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        raise NotImplementedError('Not implemented yet.')

    def get_classname(self) -> str:
        return super().get_classname()
    
    @staticmethod
    def name() -> str:
        return 'py2htmlMedia'


class Image(Media):
    
    def __init__(self, path: str, alt='Image', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.path = path
        self.alt = alt

    def __repr__(self) -> str:
        self.save_asset()
        return f'<img class="py2htmlImage {super().get_classname()}" src="{self.path}" alt="{self.alt}"{self.get_style()}>'
    
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

    @staticmethod
    def name() -> str:
        return 'py2htmlImage'