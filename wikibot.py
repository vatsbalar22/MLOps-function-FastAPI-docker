from mylib.bot import scrape
import click

@click.command()
@click.option('--name',help='webpage want to scrape')

def cli(name):
    result = scrape(name)
    click.echo(click.style(f'{result} :' ,bg='yellow', fg='black'))

if __name__ == '__main__':
    cli()


    
