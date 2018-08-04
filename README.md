# tellMe
A simple command line tool to quickly retrieve information without having to load a browser or other program.

## Setup
You'll need Python 3 and all of the modules listed in requirements.txt.

In order to use the weather module, you'll need to sign up for an API key at Mapquest and OpenWeatherMap, and then set those API keys as 'MQKey' (for Mapquest) and 'WTH' (for OpenWeatherMap) environment variables. You could also just declare them in the weather.py module if you don't want to use environment variables.

Similarly, in order to use the reddit module, you'll need to set up an account and then claim an API key. The module uses 4 environment variables in order to access the API: 'RNAME' (reddit username), 'RPASS' (reddit password), 'RAPP' (the key associated with your app), and 'RSCRT' (the secret key reddit gives you for your app). 

If it's your first time using the program, you can run `tellme.py config new` to generate a new configuration file, and then you can edit the values either through this program or by editing the 'tmconfig.ini' file.

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

**fx** - Shows the value of various currencies in comparison to USD.

    `tellme.py fx`  # Shows a list of currency values

**reddit** - Grabs the specified number of headlines from specified subreddit.

    `tellme.py reddit python 10`  # Grabs 10 top headlines from the Python subreddit

**stock** - Finds the most recent high and low of a desired stock.

    `tellme.py stock AMD` # Shows the most recent high and low value for AMD's stock

**zones** - Displays the time in various time zones. 

    `tellme.py zones`  # Shows time in a number of time zones

**timeleft** - Calculates the amount of years and days you have left to live. Arguments are: age you expect to die, year of birth, month of birth, day of birth.

    `tellme.py timeleft 65 1982 7 23`  # Shows how many years and days left until someone born in 1982 turns 65
    
