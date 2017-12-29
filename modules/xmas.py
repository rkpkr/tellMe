import datetime

def days_till_xmas():
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    if month == 12 and day == 25:
        print('\nMerry Christmas!')
        return True
    elif month == 12 and day > 25:
        year += 1
        d = datetime.date(year, 12, 25) - datetime.date.today()
        print('\nThere are ' + str(d.days) + ' days until Christmas.')
        return True
    else:
        d = datetime.date(year, 12, 25) - datetime.date.today()
        print('\nThere are ' + str(d.days) + ' days until Christmas.')
        return True
        

if __name__ == '__main__':
    days_till_xmas()
