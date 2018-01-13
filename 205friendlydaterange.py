from datetime import datetime, timedelta

def friendly_date(dates):
    dates = [x for x in dates.split(' ')]
    dates = [datetime.strptime(x, '%Y-%m-%d') for x in dates]
    date_1, date_2 = dates[0], dates[1]
    f = lambda x: 'st' if x.day % 10 == 1 else 'nd' if x.day % 10 == 2 else 'rd' if x.day % 10 == 3 else 'th'

    if date_1 == date_2:
        print("%s %d%s, %d" % (date_1.strftime("%B"), date_1.day, f(date_1), date_1.year) ) 
    elif date_1.year == datetime.now().year and date_1 + timedelta(days=365) > date_2:
        print("%s %d%s - %s %d%s" % (date_1.strftime("%B"), date_1.day, f(date_1), date_2.strftime("%B"), date_2.day, f(date_2)))
    else:
        print("%s %d%s, %d - %s %d%s, %d" % (date_1.strftime("%B"), date_1.day, f(date_1), date_1.year, date_2.strftime("%B"), date_2.day, f(date_2), date_2.year))


if __name__ == "__main__":
    # input_1 = '2015-07-01 2015-07-04'
    input_1 = '2015-07-04 2015-07-04'
    input_2 = '2018-07-01 2018-07-04'
    input_3 = '2015-12-01 2016-02-03'
    input_4 = '2015-12-01 2017-02-03'
    input_5 = '2016-03-01 2016-05-05'
    input_6 = '2017-01-01 2017-01-01'
    input_7 = '2022-09-05 2023-09-04'
    friendly_date(input_1)
    friendly_date(input_2)
    friendly_date(input_3)
    friendly_date(input_4)
    friendly_date(input_5)
    friendly_date(input_6)
    friendly_date(input_7)