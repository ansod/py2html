from src.py2html import Py2html
from src.components import Component, Hstack, Vstack, Text, Link, Button, Image
from src.actions import Hover
from src.rules import Rule

def header() -> Component:
    return Hstack(
        Text('Name', size='1.5em', color='#f1faee', font='Verdana'),
        Hstack(
            Link(
                'https://www.google.com',
                Text('Home', size='1.5em', color='#f1faee', padding='0 1em 0 0', font='Verdana', classname='nav'),
                style='none'
            ),
            Link(
                'https://www.youtube.com',
                Text('About', size='1.5em', color='#f1faee', padding='0 0 0 1em', font='Verdana', classname='nav'),
                style='none'
            ),
            padding='3em',
        ),
        classname='header',
        width='100%',
        height='10vh',
        hlayout='space-between',
        vlayout='center',
        padding='0 0 0 2em'
    )

def footer() -> Component:
    return Hstack(
        Hstack(
            Text('&#128175; Made with', size='1.1em', color='#f1faee'),
            Link('https://www.github.com/ansod/py2html', text='py2html', size='1.1em', color='#f1faee'),
            width='195px',
            hlayout='space-between'
        ),
        width='100%',
        height='20vh',
        hlayout='center',
        vlayout='center'
    )

def index() -> Component:
    return Vstack(
        header(),
        Hstack(
            Vstack(
                Text('My page', size='2.5em', color='#f1faee', padding='1em 0 0 0'),
                Vstack(
                    Text('This is some text that describes something about this website. Here is some more text.', color='#f1faee', align='center'),
                    padding='2em 1em 0 1em'
                ),
                bg='#ccdbfd',
                width='18%',
                height='40vh',
                hlayout='center',
                rounded='15px 0 0 15px',
                shadow='8px 8px 15px #91a4d2'
            ),
            Vstack(
                Link(
                    'https://www.github.com/ansod/py2html',
                    Button(
                        Hstack(
                            Image('./github-mark-white.png', width='25px', height='25px'),
                            Text('Click here', size='18px', color='#f1faee'),
                            hlayout='space-around',
                            vlayout='center',
                            width='140px'
                        ),
                        classname='cool_button',
                        bg='#ccdbfd',
                        padding='1em',
                        rounded='6px',
                        shadow='5px 5px #abc4ff'
                    ),
                    style='none'
                ),
                bg='#f1faee',
                width='35%',
                height='40vh',
                hlayout='center',
                vlayout='center',
                rounded='0 15px 15px 0',
                shadow='20px 8px 15px #91a4d2'
            ),
            width='100%',
            height='70vh',
            hlayout='center',
            vlayout='center'
        ),
        footer(),
        bg='#abc4ff',
        width='100%',
        height='100vh'
    )
        


site = Py2html('Test site')
index_view = site.add_view('index', index)
index_view.add_action(Hover(shadow='3px 3px #abc4ff', transform='translate(2px,2px)'), 'cool_button')
index_view.add_action(Hover(color='#5d76b3'), 'nav')
index_view.add_rule(Rule(font='Verdana'), component=Text)
index_view.add_rule(Rule(font='Verdana'), component=Link)
site.compile()