import click
import requests
from datetime import datetime
from terminaltables import AsciiTable
from colorama import Fore, Back, Style, init
from time import gmtime, strftime

url = "https://data.sfgov.org/resource/jjew-r69b.json"

@click.command()

def get_trucks():
    """Gets all the San Fransisco food trucks that are open now"""

    def _add_elements(truck, table_data):
        """
        Appends truck data onto a table for consumption
        :param truck: JSON object
        :param table_data:
        :return:
        """
        table_data.append([truck["applicant"], truck["location"]])

    init(autoreset=True)

    click.echo('Welcome to the Food Truck Finder!\n')

    current_datetime = datetime.now()
    click.echo(f"Today is {(current_datetime.strftime('%A %d. %B %Y %H:%m'))}")
    day = current_datetime.isoweekday()
    if day == 7:
        day = 0
    payload = {
        "dayorder":day,
        "$order":"applicant",
        "$where":f"start24 < '{(current_datetime.strftime('%H:%m'))}' and \
        end24 > '{(current_datetime.strftime('%H:%m'))}'",
    }
    r = requests.get(url, params=payload)
    table_data = [
        ['Name', 'Address']
    ]
    if r.status_code == requests.codes.ok:
        start = 0
        length=len(r.json())
        for truck in r.json():
            _add_elements(truck, table_data)
            start += 1
            if start == length:
                table = AsciiTable(table_data)
                click.echo(table.table)
            if start%10 == 0:
                table = AsciiTable(table_data)
                click.echo(Fore.MAGENTA + (table.table))
                value = click.prompt('Would you like the next 10 trucks? (y/n)', type=str)
                if value.lower() == 'n':
                    click.echo('Thank you for using the Food Truck Finder!')
                    break
                else:
                    table_data = [
                        ['Name', 'Address']
                    ]


    else:
        click.echo('There has been an error.  Please try again later.')

    # display name and address alphabetically by name
