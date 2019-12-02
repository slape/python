from setuptools import setup

setup(
    name='new',
    version='1.0',
    py_modules=['new'],
    install_requires=[
        'Click',
        'cookiecutter',
    ],
    entry_points='''
        [console_scripts]
        new=new:cli
    '''
)