import configparser
import os

def default_config():
    config = configparser.ConfigParser()
    config['Cryptocurrency'] = {'BTC': .0025}
    config['Weather'] = {'Town': 'Caribou',
                        'Area': 'Maine'}
    config['Hacker News'] = {'Articles': 10}
    with open('tmconfig.ini', 'w') as configfile:
        config.write(configfile)

def import_config():
    if os.path.isfile('tmconfig.ini'):
        config = configparser.ConfigParser()
        config.read('tmconfig.ini')
        return config
    else:
        return False

if __name__ == '__main__':
    default_config()
    cf = import_config()
    print(cf['Cryptocurrency']['BTC'])
