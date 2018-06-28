import click
import requests
from datetime import datetime
from time import gmtime, strftime





url = "https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b"

@click.command()
@click.option('--time', default=1, prompt='The time you want to get food in format HH:MM', help='The time you would like food today')
@click.option('--date', prompt='The date you want to get food in format MMDD',
              help='The date you want food')
def get_trucks(time=None, date=None):
    """Simple program that greets NAME for a total of COUNT times."""
    days_of_week = {
        'Monday':'1',
        'Tuesday':'2',
        'Wednesday':'3',
        'Thursday':'4',
        'Friday':'5',
        'Saturday':'6',
        'Sunday':'7'
    }
    # query params dayorder=5 gives friday

    if not time and not date:
        current_datetime = datetime.now()
    payload = {'dayorder':current_datetime.weekday(),                       '$where':f"start24 < {current_datetime.strftime('%H:%m')}",
               ""$where":f"end24 > {current_datetime.strftime('%H:%m')}", $order":"applicant"}

    r = requests.get(url, params=payload)

    # display name and address alphabetically by name
