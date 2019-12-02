import click

class Config(object):
    
    def __init__(self):
        self.v = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('-v', is_flag=True, 
            help='Enable Verbose Mode.')
@click.option('-h', type=click.Path())
@pass_config
def cli(config, v, h):
    config.v = v
    if h is None:
        h = '.'
    config.h = h

@cli.command()
@click.option('-s', default='world',
            help='This is the thing that is greeted.')
@click.option('-r', default=1,
            help='How many times your are greeted.')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
@pass_config
def say(config, s, r, out):
    """This script greets you. Pass a file as an argument to write to that file."""
    if config.v:
        click.echo('Verbose Mode Enabled.')
    click.echo(f'Home directory is {config.h}.')
    if r:
        for i in range(r):
            click.echo(f"Hello {s}!", file=out)
    else:
        click.echo(f"Hello {s}!", file=out)