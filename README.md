# Food Truck CLI

## About
If you're hungry, we can find a food truck for you.


This food truck CLI will render the first ten food trucks in San Francisco that are open now in alphabetical order.  
After the first ten are rendered in a table, you will receive a prompt asking if you would like to see the next ten 
until all of the food trucks have been rendered or you respond with an 'n'.

A CLI made using [Python](Welcome to Python.org), [Click](http://click.pocoo.org/5/), 
[Requests](http://docs.python-requests.org/), [Terminal Tables](https://robpol86.github.io/terminaltables/), and 
[Colorama](https://pypi.org/project/colorama/) for style.

## Setup
__In the main directory in your terminal run this command__

```bash
pipenv install
```
This will set up your pip environment.

_Note:  If you don't already have Pipenv and you have a Mac, you can install it with 'brew install pipenv'.  
If you don't feel like doing that, I have added a requirements.txt in the same directory.  You can use that to set up 
your virtual environment.  I believe you can run all of the same commands in your virtual environment using pip instead 
of pipenv. Also, I am using 'f strings' which is incompatible with versions less than 3.6._

__Activate your virtual environment__

```bash
pipenv shell
```

## Build

```bash
pipenv install --editable .
```

## Run
In your terminal with your shell (virtual environment) activated:
```bash
food_truck
```

## More Info

If I were to build upon this CLI, I would use more error handling for unexpected results and responses. I would also add
 some more features for the user to interact with.  For example, I would like to give the user the option to choose the 
 day and time for the food truck output as well as the option to get phone numbers.  The Click library gives a lot of 
 options for different flags that you can apply to customize the user's experience.  A help option would be the most 
 useful, in my opinion.
 
As a web application, I would change this design completely, but probably use the same queries to get the data.  Since 
the data is being consumed in the same way, I would continue to use the same url. If a one page application is all that
is required, I could render the first ten on that page with pagination.  In addition, the time in San Francisco is always
the same, so I would only have to update the trucks depending on that time zone.  I would probably set up a timed event 
  to update the page every so often (maybe 15 minutes).  Right now, my CLI takes the user's time
and date and uses it to find the food trucks, but it may not be in the correct time zone. 