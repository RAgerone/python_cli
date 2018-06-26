import click
import requests
from time import gmtime, strftime





url = "https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b"

@click.command()
@click.option('--time', default=1, prompt='The time you want to get food in format HH:MM', help='The time you would like food today')
@click.option('--date', prompt='The date you want to get food in format MMDD',
              help='The date you want food')
def get_trucks(time=None, date=None):
    """Simple program that greets NAME for a total of COUNT times."""
    if not time and not date:
        date, time = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split()
    # for x in range(count):
    #     click.echo('Hello %s!' % name)

if __name__ == '__main__':
    get_trucks()