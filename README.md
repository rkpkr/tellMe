# tellMe
A simple command line tool to quickly retrieve information without having to load a browser or other program.

## Setup
You'll need Python 3 and all of the modules listed in requirements.txt.

In order to use the weather module, you'll need to sign up for an API key at Mapquest and OpenWeatherMap, and then set those API keys as 'MQKey' (for Mapquest) and 'WTH' (for OpenWeatherMap) environment variables. You could also just declare them in the weather.py module if you don't want to use environment variables.

If it's your first time using the program, you can run `tellme.py config` to generate a new configuration file, and then you can edit the values either through this program or by editing the 'tmconfig.ini' file.

For easy use of this tool, place the script in your PATH, and you can call it anywhere.
In Windows, you could convert the script to an EXE using something like cx_Freeze and
then place the EXE in your path, allowing you to call it without the .py extension.

## Usage
The basic usage is simple: `python tellme.py command arguments`.

In Linux, you may need to explicitly use python3 instead of python to run the script.
The commands are listed in the help, called by giving the -h or --help arguments when
you run the script. 

Here's a simple example of using it:

`python tellme.py coin btc GBP`

That command will check the Bitcoin price in British Pounds and display it on screen.

## Modules

**config** - Used to create a new config file or add/edit values in existing config. Calling config without arguments will create a new config file with some default values. Similarly, calling config with the argument "new" will perform the same function. 


    `tellme.py config weather town fairbanks`  # Adds fairbanks as town in weather section

**coin** - Checks the cryptocurrency price in specified currency. Currency codes are three letters, e.g. JPY for Japanese yen or USD for U.S. Dollars

    `tellme.py coin eth nzd`  # Finds the value of Ethereum in New Zealand Dollars

**wth** - Checks the local weather. The arguments it takes are town and area. If you provide a town without an area, it is set to default the area to Maine, so watch out for that. If you want to search for cities without specifying a state/country/area, you'll have to modify the script to remove the area argument. Also note that the format is specifying the town, then a space, then the area. If you're searching for a place that is more than one word, avoid putting spaces in it. For instance, if you're looking for the weather in Los Angeles, try 'tellmy.py wth losangeles california'. 

    `tellme.py wth caribou maine`  # Finds the weather in Caribou, Maine

**xmas** - Calculates the days left until Christmas.

    `tellme.py xmas`  # Tells how many days until Christmas

**hnews** - Grabs # of top headlines from Hacker News, where # is specified by you.

    `tellme.py hnews 10`  # Retrieves the top 10 headlines from Hacker News

**fx** - Finds the value of target currency in base currency you specify.

    `tellme.py fx usd nzd'  # Shows the value of USD in NZD

**zones** - Displays the time in various time zones. 

    `tellme.py zones`  # Shows time in a number of time zones

**timeleft** - Calculates the amount of years and days you have left to live. Arguments are: gender, year of birth, month of birth, day of birth.

    `tellme.py timeleft M 1912 7 23`  # Days left for a male born on 7/23/1912
    

## Future Plans

* Add Reddit module
