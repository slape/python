import click
from cookiecutter.main import cookiecutter

@click.command() 
def cli():
    '''Create a new cli tool.'''
    click.echo('Creating your cli tool project directory and files.')
    project = input('Project Name: ').lower()
    
    cookiecutter('https://github.com/slape/cli_template',
    no_input=True,
    extra_context={
        "project" : project,
    })