import click
import requests
from datetime import datetime
from terminaltables import AsciiTable
from time import gmtime, strftime





url = "https://data.sfgov.org/resource/jjew-r69b.json"

@click.command()
@click.option('--time', default=1, prompt='The time you want to get food in format HH:MM', help='The time you would like food today')
@click.option('--date', prompt='The date you want to get food in format MMDD',
              help='The date you want food')



def get_trucks(time=None, date=None):
    """Simple program that greets NAME for a total of COUNT times."""

    # query params dayorder=5 gives friday

    # if not time and not date:
    def add_elements(truc, table_data):
        table_data.append([truck["applicant"], truck['location']])
        click.echo(truck)
        table = AsciiTable(table_data)
        click.echo(table)
    current_datetime = datetime.now()

    payload = {
        "dayorder": current_datetime.weekday(),
        '$where': ['banana',
            f"start24 < '{current_datetime.strftime('%H:%m')}'",
            f"end24 > '{current_datetime.strftime('%H:%m')}'"
    ],
        "$order":"applicant"
    }
    click.echo(payload)
    r = requests.get(url, params=None)
    click.echo(r.url)
    table_data = [
        ['Name', 'Address']
    ]
    click.echo(url)
    start = 0
    ten_more = True
    click.echo(r)
    for truck in r.json():
        add_elements(truck, table_data)
        start += 1
        if start%10 == 0:
            table = AsciiTable(table_data)
            click.echo(table)


    # display name and address alphabetically by name
