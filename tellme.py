import click

@click.group()
def cli():
    pass

@cli.command()
def btc():
    click.echo('The current bitcoin price is over 9000.')
