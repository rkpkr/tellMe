# tellMe
A simple command line tool to quickly retrieve information without having to load a browser or other program.

## Setup
The only things you need to run this tool so far are Python 3 and the requests module.
I used Python 3.5, but I'm pretty sure there aren't any features that wouldn't work in
other versions of Python 3.

For easy use of this tool, place the script in your PATH, and you can call it anywhere.
In Windows, you could convert the script to an EXE using something like cx_Freeze and
then place the EXE in your path, allowing you to call it without the .py extension.

## Usage
The basic usage is simple: `python tellme.py command arguments`.
In Linux, you may need to explicitly use python3 instead of python to run the script.
The commands are listed in the help, called by giving the -h or --help arguments when
you run the script. 

Here's a simple example of using it:
`python tellme.py btc GBP`

That command will check the Bitcoin price in British Pounds and display it on screen.

## Modules

btc - Checks the Bitcoin price in specified currency. Currency codes are three letters,
e.g. JPY for Japanese yen or USD for U.S. Dollars
    `tellme.py btc currency`

wth - Checks the local weather. Currently only works for the two hard-coded examples I
have - one for Caribou, ME, and one for Galveston, TX.
    `tellme.py wth gal`

xmas - Calculates the days left until Christmas.
    `tellme.py xmas`

hnews - Grabs # of top headlines from Hacker News, where # is specified by you.
    `tellme.py hnews 10`

timeleft - Calculates the amount of years and days you have left to live. Arguments are: gender, year of birth, month of birth, day of birth.
    `tellme.py timeleft M 1912 7 23`
    

## Future Plans

* Fix the weather module.
* Add Reddit module.
* Expand cryptocurrency module.
* Add currency exchange rates module.
* Add ability to use a configuration file.


