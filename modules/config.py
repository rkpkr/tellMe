import configparser
import os

def default_config():
    config = configparser.ConfigParser()
    config['crypto'] = {'BTC': .0025,
                        'def_coin': 'BTC',
                        'def_fiat': 'USD'}
    config['weather'] = {'Town': 'Caribou',
                        'Area': 'Maine'}
    config['hnews'] = {'Articles': 10}
    config['forex'] = {'Base': 'USD',
                      'Target': 'JPY'}
    config['reddit'] = {'Subreddit': 'python',
                        'Headlines': 10}
    with open('tmconfig.ini', 'w') as configfile:
        config.write(configfile)

def import_config():
    if os.path.isfile('tmconfig.ini'):
        config = configparser.ConfigParser()
        config.read('tmconfig.ini')
        return config
    else:
        return False

def add_config(section, name, value):
    if os.path.isfile('tmconfig.ini'):
        config = configparser.ConfigParser()
        config.read('tmconfig.ini')
        if section in config.keys():
            config[section][name] = value
#        if section == 'Cryptocurrency':
#            config['Cryptocurrency'][name] = value
#        elif section == 'Weather':
#            config['Weather'][name] = value
        else:
            print('Section not found.')
            return False
        with open('tmconfig.ini', 'w') as configfile:
            config.write(configfile)
    else:
        print('Configuration file not found.')
        return False 

if __name__ == '__main__':
    default_config()
    add_config('Cryptocurrency', 'LTC', '.2')
    cf = import_config()
    print(cf['Cryptocurrency']['BTC'])
