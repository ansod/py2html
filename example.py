from src.py2html import Py2html
from src.components import Component, Hstack, Vstack, Text, Link

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
            padding='2em',
        ),
        bg='#1d3557',
        width='100%',
        height='10vh',
        hlayout='space-between',
        vlayout='center',
        padding='0 0 0 1em'
    )

def footer() -> Component:
    return Vstack(
        Text('&#128175; Made with py2html', color='#f1faee'),
        bg='#a8dadc',
        width='100%',
        height='20vh',
        hlayout='center',
        vlayout='center'
    )

def index() -> Component:
    return Vstack(
        header(),
        Vstack(
            Vstack(
                Text('My page', size='2.5em', color='#000000', padding='1em 0 0 0'),
                bg='#ffffff',
                width='20%',
                height='30vh',
                hlayout='center',
                rounded='15px'
            ),
            width='100%',
            height='70vh',
            hlayout='center',
            vlayout='center'
        ),
        footer(),
        bg='#f1faee',
        width='100%',
        height='100vh'
    )
        


site = Py2html('Test site')
site.add_view('index', index)
site.compile()