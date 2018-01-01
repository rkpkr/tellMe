import datetime
from collections import OrderedDict

def time_zones():
    zones = OrderedDict([('Baker Island', (-12,0)),
                        ('America (Alaska)', (-9,0)),
                        ('America (Texas)', (-6,0)),
                        ('America (Maine)', (-5,0)),
                        ('Canada (Newfoundland)', (-3, -30)),
                        ('United Kingdom (UTC)', (0,0)),
                        ('France', (1,0)),
                        ('Finland', (2,0)),
                        ('Russia (Moscow)', (3,0)),
                        ('India', (5, 30)),
                        ('China', (8,0)),
                        ('Japan', (9,0)),
                        ('Australia (Canberra)', (11,0)),
                        ('New Zealand (Wellington)', (13,0)),
                        ('Kiribati (Line Islands)', (14,0))])
    utc = datetime.datetime.utcnow()
    utc_hour = utc.hour
    utc_minutes = utc.minute
    for zone, times in zones.items():
        hour_dif, mins = minute_check(utc_minutes, times[1])
        zoned_hour = hour_check(utc_hour, times[0], hour_dif)
        fin_hour, AMPM = am_pm(zoned_hour)
        if len(str(mins)) == 1:
            mins = '0' + str(mins)
        print(zone.ljust(30) + str(fin_hour).rjust(5) + ':' + str(mins) + ' ' + AMPM) 

def minute_check(minutes_now, tz_minutes):
    dif_hour = 0
    new_minutes = 0
    if minutes_now + tz_minutes >= 60:
        dif_hour += 1
        new_minutes = (minutes_now + tz_minutes) - 60
    elif minutes_now + tz_minutes < 0:
        dif_hour = -1
        new_minutes = (minutes_now + tz_minutes) + 60
    else:
        new_minutes = minutes_now + tz_minutes
    adjusted = (dif_hour, new_minutes)
    return adjusted
        
def hour_check(hour_now, tz_offset, minutes_offset):
    if (hour_now + tz_offset + minutes_offset) >= 24:
        cur_hour = (hour_now + tz_offset + minutes_offset) - 24
    elif (hour_now + tz_offset + minutes_offset) < 0:
        cur_hour = (hour_now + tz_offset + minutes_offset) + 24
    else:
        cur_hour = hour_now + tz_offset + minutes_offset
    return cur_hour
            
def am_pm(hour):
    if hour > 12:
        new_hour = hour - 12
        ampm = 'PM'
    elif hour == 12:
        new_hour = hour
        ampm = 'PM'
    elif hour == 0:
        new_hour = 12
        ampm = 'AM'
    else:
        new_hour = hour
        ampm = 'AM'
    final_time = (new_hour, ampm)
    return final_time

if __name__ == '__main__':
    print(minute_check(31, -41))
    print(minute_check(31, 41))
    print(minute_check(29, 1))
    print(minute_check(59, -41))
    print(hour_check(12, 5, 0))
    print(hour_check(15, 7, 1))
    print(hour_check(11, -12, -1))
    print(hour_check(22, 5, 0))
    print(hour_check(23, 1, 0))
    print(am_pm(22))
    print(am_pm(2))
    print(am_pm(12))
    print(am_pm(0))
    time_zones()
