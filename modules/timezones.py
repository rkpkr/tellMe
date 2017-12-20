import datetime
from collections import OrderedDict

def time_zones():
    today = datetime.datetime.now()
    local_hour = today.hour
    minutes = today.minute
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    utc = datetime.datetime.utcnow()
    utc_hour = utc.hour

    zones = OrderedDict([('America (Alaska)', -9),
                        ('America (Houston)', -6),
                        ('America (New York)', -5),
                        ('United Kingdom (UTC)', 0),
                        ('France', 1),
                        ('Finland', 2),
                        ('Russia (Moscow)', 3),
                        ('China', 8),
                        ('Japan', 9),
                        ('Australia (Canberra)', 11),
                        ('New Zealand (Wellington)', 13)])

    
    for z, t in zones.items():
        if (utc_hour + t) >= 24:
            cur_hour = (utc_hour + t) - 24
        elif (utc_hour + t) < 0:
            cur_hour = (utc_hour + t) + 24
        else:
            cur_hour = utc_hour + t
        if cur_hour > 12:
            cur_hour = cur_hour - 12
            ampm = 'PM'
        elif cur_hour == 12:
            ampm = 'PM'
        elif cur_hour == 0:
            cur_hour = 12
            ampm = 'AM'
        else:
            ampm = 'AM'
        print(z.ljust(30) + str(cur_hour).rjust(5) + ':' + str(minutes) + ' ' + ampm) 



if __name__ == '__main__':
    time_zones()
