import datetime
import math
import time


def main():
    get_current_time()
    get_direction()


def get_direction():
    print("\n[STARTING INFORMATION PROCESS]")
    while True:
        print("To analise an individual type: '1'. To the relationship between 2 people type: '2'")
        action = input("Enter '1' or '2': ")
        if action == "1":
            print(' \nENTER INFORMATION BELOW')
            global p1
            p1 = create_people()
            print("[SUCCESS]")
            break
        elif action == '2':
            print(" \nENTER INFORMATION FOR PERSON 1 BELOW")
            global p2
            p2 = create_people()
            print("\nENTER INFORMATION FOR PERSON 2 BELOW")
            global p3
            p3 = create_people()
            compare(p2, p3)
            break

        else:
            print("[INVALID OPTION]")
            time.sleep(0.5)
            print("[PLEASE TRY AGAIN]")
            time.sleep(0.5)


def get_current_time():
    print("[FETCHING CURRENT DATE]")
    global month_average
    month_average = 30.4375
    now = datetime.datetime.now()
    day = now.day / 365.25
    month = (now.month - 1) / 12
    year = now.year
    global nowTime
    nowTime = day + month + year
    time.sleep(0.5)
    print('Current date: ', end='')
    year_to_date(nowTime)
    time.sleep(0.5)


class Person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.day = int(input("Enter birth date (day of month): "))
        self.month = int(input("Enter birth month (number): "))
        self.year = int(input("Enter birth year: "))

        while True:
            self.gender = input("Enter gender 'male' or 'female': ")
            if (self.gender == 'male') or (self.gender == 'female'):
                break
            else:
                print("[INVALID SELECTION]", end='       ')
                time.sleep(0.5)
                print('[PLEASE TRY AGAIN]')
                time.sleep(0.5)

    def calc_age(self):
        print('[CALCULATING AGE]')
        time.sleep(0.5)
        self.birthday = (self.day / 365.25 + ((self.month - 1) / 12) + self.year)
        self.age = nowTime - self.birthday
        print(self.name, "'s birthday is: ", end='', sep='')
        year_to_date(self.birthday)
        print(self.name, "'s age is: ", end='', sep='')
        year_to_age(self.age)
        return self.age

    def calc_crit_age(self, age):
        if self.gender == "male":
            self.crit_age = (age / 2) + 7
            print(self.name,"'s critical age is: ", end='', sep='')
            year_to_age(self.crit_age)

        elif self.gender == "female":
            self.crit_age = (age - 7) * 2
            print(self.name, "'s critical age is: ", end='', sep='')
            year_to_age(self.crit_age)
        else:
            print("gender not applicable")


def create_people():
    p = Person()
    p.calc_crit_age(p.calc_age())
    return p


def create():
    print("Creating person 1... ")
    global p1
    p1 = create_people()
    print("Creating person 2... ")
    global p2
    p2 = create_people()


def calc_match_age(p_1, p_2):
    age_diff = p_1.age - p_2.age
    m = p_1.age
    f = p_2.age
    m_match = 2 * age_diff + (2 * 7)
    f_match = m_match - age_diff
    print(p_1.name, "'s age: ", end='', sep='')
    year_to_age(m)
    print(p_2.name, "'s age: ", end='', sep='')
    year_to_age(f)
    print(p_1.name, "'s match age: ", end='', sep='')
    year_to_age(m_match)
    print(p_2.name, "'s match age: ", end='', sep='')
    year_to_age(f_match)
    return m_match


def calc_match_date(age, p_1):
    time_from_present = age - p_1.age
    match_date = nowTime + time_from_present
    from_now_diff = match_date - nowTime
    print("The date at which this is safe: ", end='')
    year_to_date(match_date)
    if from_now_diff >= 0:
        print("This will be safe in: ", end='')
        year_to_age(from_now_diff)
    else:
        print("This was safe: ", end='')
        year_to_age(from_now_diff)


def is_match_possible(p_1, p_2):
    if p_2.age >= p_1.crit_age:
        print("It is SAFE for this pair at this time.")
    else:
        print("It is NOT SAFE for this pair at this time.")


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
    total_days = math.sqrt(math.pow((time * 365.25), 2))
    year = 0

    t_year_days = total_days
    while t_year_days > 366:
        year += 1
        t_year_days -= 365.25

    month = 0
    t_month_days = t_year_days
    while t_month_days >= month_average:
        t_month_days -= month_average
        month += 1

    day = round(t_month_days)

    if time <= 0:
        print(year, 'years,', month, 'months and', day, 'days ago.')

    else:
        print(year, 'years,', month, 'months and', day, 'days.')


def compare(p_1, p_2):
    print("\n[COMPILING DATA]", end='           ')
    time.sleep(0.5)
    print("[COMPLETE]")
    is_match_possible(p_1, p_2)
    calc_match_date(calc_match_age(p_1, p_2), p_1)


main()





