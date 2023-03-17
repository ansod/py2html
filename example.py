from src.py2html import Py2html
from src.components import Component, Hstack, Vstack, Text, Link

def header() -> Component:
    return Hstack(
        Text('Name', size='1.5em', color='#ffffff'),
        Hstack(
            Link(
                Text('Home', size='1.5em', color='#ffffff'),
                href='https://www.google.com'
            ),
            Link(
                Text('About', size='1.5em', color='#ffffff'),
                href='https://www.youtube.com'
            )
        ),
        bg='#000000',
        width='100%',
        height='10vh',
        hlayout='space-between',
        vlayout='center'
    )

def footer() -> Component:
    return Vstack(
        Text('Made with py2html', color='#ffffff'),
        bg='#000000',
        width='100%',
        height='20vh',
        hlayout='center',
        vlayout='center'
    )

def index() -> Component:
    return Vstack(
        header(),
        Vstack(
            Text('My page', size='2.5em', color='#ffffff'),
            width='100%',
            height='70vh',
            hlayout='center',
            vlayout='center'
        ),
        footer(),
        bg='#ffffff',
        width='100%',
        height='100vh'
    )
        


site = Py2html('Test site')
site.add_view('index', index)
site.compile()