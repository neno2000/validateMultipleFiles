from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'ValidateBoomi.py'}],
    options={
        'py2exe':
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
        }
    }
)