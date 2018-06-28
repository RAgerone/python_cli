from setuptools import setup

setup(
    name='food_truck',
    version='0.1',
    py_modules=['food_truck'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        food_truck=food_truck:get_trucks
    ''',
)
