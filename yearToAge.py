

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
yearTime = day / 365.25 + (month-1) / 12 + year
month_average = 30.4375


def year_to_date(time):
    total_days = time * 365.25
    year = 0

    t_year_days = total_days
    while t_year_days > 366:
        year += 1
        t_year_days -= 365.25

    month = 1
    t_month_days = t_year_days
    while t_month_days > 31:
        t_month_days -= month_average
        month += 1

    day = round(t_month_days)

    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    print(day, '-', month_name[month - 1], '-', year, sep='')


def year_to_age(time):
    total_days = time * 365.25
    year = 0

    t_year_days = total_days
    while t_year_days > 366:
        year += 1
        t_year_days -= 365.25

    month = 1
    t_month_days = t_year_days
    while t_month_days > 31:
        t_month_days -= month_average
        month += 1

    day = round(t_month_days)

    print(year, 'years,', month, 'months and', day, 'days.')



year_to_date(yearTime)

year_to_age(yearTime)
