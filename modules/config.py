import configparser

def default_config():
    config = configparser.ConfigParser()
    config['Cryptocurrency'] = {'BTC': .0025}
    config['Weather'] = {'Town': 'Caribou',
                        'Area': 'Maine'}
    config['Hacker News'] = {'Articles': 10}
    with open('tmconfig.ini', 'w') as configfile:
        config.write(configfile)

def import_config():
   pass 


if __name__ == '__main__':
    default_config()
