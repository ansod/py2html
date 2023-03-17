from src.py2html import Py2html
from src.components import Component, Hstack, Vstack, Text, Link, Button

def header() -> Component:
    return Hstack(
        Text('Name', size='1.5em', color='#f1faee'),
        Hstack(
            Link(
                Text('Home', size='1.5em', color='#f1faee', padding='0 1em 0 0'),
                href='https://www.google.com',
                style='none'
            ),
            Link(
                Text('About', size='1.5em', color='#f1faee', padding='0 0 0 1em'),
                href='https://www.youtube.com',
                style='none'
            ),
            padding='3em',
        ),
        width='100%',
        height='10vh',
        hlayout='space-between',
        vlayout='center',
        padding='0 0 0 2em'
    )

def footer() -> Component:
    return Vstack(
        Text('&#128175; Made with py2html', size='1.1em', color='#f1faee'),
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
                bg='#ccdbfd',
                width='18%',
                height='40vh',
                hlayout='center',
                rounded='15px 0 0 15px',
                shadow='8px 8px 15px #91a4d2'
            ),
            Vstack(
                Link(
                    Button(
                        Text('Click here', size='18px', color='#f1faee'),
                        bg='#ccdbfd',
                        padding='1em',
                        rounded='6px',
                        shadow='5px 5px #abc4ff'
                    ),
                    href='https://www.github.com/ansod/py2html',
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
site.add_view('index', index)
site.compile()