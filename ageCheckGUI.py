import datetime
import math


def main():     # main method
    get_current_time()
    # p1 = Person("Jonno", 1, 6, 2001, "male")
    # p2 = Person("Sheila", 1, 6, 2002, "female")
    # match_1, match_2 = calc_match_age(p1, p2)
    # print(match_1)
    # print(match_2)
    # match_date, time_to_match = calc_match_date(match_1, p1)
    # print(year_to_date(match_date))
    # possible = is_match_possible(p1, p2)
    # print(possible)


def get_current_time():     # fetches current date, converts it to date in terms of years
    now = datetime.datetime.now()
    day = now.day / 365.25
    month = (now.month - 1) / 12
    year = now.year
    global nowTime
    nowTime = day + month + year
    return nowTime


class Person:
    def __init__(self, name, day, month, year, gender):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.gender = gender
        self.birthday = (self.day / 365.25 + ((self.month - 1) / 12) + self.year)
        self.age = nowTime - self.birthday
        self.crit_age_below = (self.age / 2) + 7
        self.crit_age_above = (self.age - 7) * 2


def create_people(name, day, month, year, gender):
    p = Person(name, day, month, year, gender)
    return p


def calc_match_age(p_1, p_2):
    if p_1.age >= p_2.age:
        age_diff = p_1.age - p_2.age
        match_1 = 2 * age_diff + (2 * 7)
        match_2 = match_1 - age_diff
        return match_1, match_2
    else:
        age_diff = p_2.age - p_1.age
        match_2 = 2 * age_diff + (2 * 7)
        match_1 = match_2 - age_diff
        return match_1, match_2


def calc_match_date(m_age, p_1):
    time_from_present = m_age - p_1.age
    match_date = nowTime + time_from_present
    from_now_diff = match_date - nowTime
    return match_date, from_now_diff


def is_match_possible(p1, p2):
    p1 = p1
    p2 = p2
    match_age_1, match_age_2 = calc_match_age(p1, p2)
    age_1 = p1.age
    age_2 = p2.age

    if (match_age_1 <= age_1) and (match_age_2 <= age_2):
        return "SAFE"
    else:
        return "NOT SAFE"


def year_to_date(time):
    total_days = time * 365.25
    year = 0

    t_year_days = total_days
    while t_year_days > 366:
        year += 1
        t_year_days -= 365.25

    month = 0
    t_month_days = t_year_days
    while t_month_days > 31:
        t_month_days -= 30.4375
        month += 1

    day = round(t_month_days)

    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    return f"{day}-{month_name[month]}-{year}"


def year_to_age(time):
    total_days = math.sqrt(math.pow((time * 365.25), 2))
    year = 0

    t_year_days = total_days
    while t_year_days > 366:
        year += 1
        t_year_days -= 365.25

    month = 0
    t_month_days = t_year_days
    while t_month_days >= 30.4375:
        t_month_days -= 30.4375
        month += 1

    day = round(t_month_days)

    return f"{year} y, {month} m, {day} d"


main()




