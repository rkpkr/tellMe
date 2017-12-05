import datetime

def time_left(gender, year, month, day):
    if gender == 'M' or gender == 'MALE' or gender == 'BOY' or gender == 'MAN':
        est_left = 82
    elif gender == 'F' or gender == 'FEMALE' or gender == 'GIRL' or gender == 'WOMAN':
        est_left = 87
    else:
        print('Invalid parameter(s).')
        return False
    cur_year = datetime.date.today().year
    cur_month = datetime.date.today().month
    cur_day = datetime.date.today().day
    if cur_month > month:
        age = cur_year - year
        years_left = est_left - age
        next_bday = datetime.date((cur_year + 1), month, day)
        to_bday = next_bday - datetime.date.today()
        days1 = to_bday.days
        days_left = days1 + ((years_left - 1) * 365)
        print('You have ' + str(years_left) +
         ' years left to live, or approximately ' + str(days_left) + ' days.')
        return None
    elif cur_month == month and cur_day >= day:
        age = cur_year - year
        years_left = est_left - age
        next_bday = datetime.date((cur_year + 1), month, day)
        to_bday = next_bday - datetime.date.today()
        days1 = to_bday.days
        days_left = days1 + ((years_left - 1) * 365)
        print('You have ' + str(years_left) +
         ' years left to live, or approximately ' + str(days_left) + ' days.')
        return None
    else:
        age = cur_year - year - 1
        years_left = est_left - age
        next_bday = datetime.date(cur_year, month, day)
        to_bday = next_bday - datetime.date.today()
        days1 = to_bday.days
        days_left = days1 + ((years_left - 1) * 365)
        print('You have ' + str(years_left) +
         ' years left to live, or approximately ' + str(days_left) + ' days.')
        return None


if __name__ == '__main__':
    time_left('M', 1999, 12, 25)
    time_left('FEMALE', 1936, 2, 1)
    time_left('gal', 2001, 9, 11)
    time_left('BOY', 2016, 12, 5)
    time_left('MAN', 1986, 10, 27)
