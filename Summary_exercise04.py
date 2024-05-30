def gen_secs():
    """ גנרטור שמפיק את כל השניות האפשריות מ-0 עד 59 """
    for sec in range(60):  # הטווח כולל 0 ועד 59
        yield sec

def gen_minutes():
    """ גנרטור שמפיק את כל הדקות האפשריות מ-0 עד 59 """
    for min in range(60):  # הטווח כולל 0 ועד 59
        yield min

def gen_hours():
    """ גנרטור שמפיק את כל השעות האפשריות מ-0 עד 23 """
    for hour in range(24):  # הטווח כולל 0 ועד 23
        yield hour


def gen_time():
    """גנרטור שמחזיר את כל השעות האפשריות ביום מ-00:00:00 עד 23:59:59"""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


import datetime

def gen_years(start=2019):
    """ גנרטור המפיק את השנה המתחילה וכל השנים ממנה והלאה """
    current_year = start
    while True:
        yield current_year
        current_year += 1

def gen_months():
    """ גנרטור המפיק את כל החודשים בשנה, מ-1 עד 12 """
    for month in range(1, 13):
        yield month

# דוגמה לשימוש בפונקציות
year_generator = gen_years()
month_generator = gen_months()

# print(next(year_generator))
# print(next(year_generator))
# print(next(month_generator))
# print(next(month_generator))


def gen_days(month, leap_year=True):
    """ גנרטור המפיק את מספר הימים בחודש נתון, תוך התחשבות בשנה מעוברת """
    # מילון שמפרט את מספר הימים בכל חודש
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }

    # בדיקה שהחודש תקף
    if 1 <= month <= 12:
        for day in range(1, days_in_month[month] + 1):
            yield day
    else:
        raise ValueError("חודש לא תקף: אנא בחר מספר חודש בין 1 ל-12")


# דוגמה לשימוש בפונקציה
# for day in gen_days(2, leap_year=True):
#     print(day)  # הדפסת כל הימים בפברואר בשנה מעוברת



def gen_date():
    """ גנרטור המחזיר חתימת תאריך מלאה בפורמט dd/mm/yyyy hh:mm:ss. """
    for year in gen_years():
        # בדיקה האם השנה היא מעוברת
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        for month in gen_months():
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"


# # דוגמה לשימוש בפונקציה
# date_generator = gen_date()
# for _ in range(10):
#     print(next(date_generator))  # הדפסת עשר תאריכים ושעות התחלתיות


def print_millionth_date():
    date_generator = gen_date()
    count = 1  # מונה לספירת האיטרציות
    while True:
        date = next(date_generator)  # מפיק תאריך הבא
        if count % 1000000 == 0:  # בדיקה אם הגענו למיליון איטרציות
            print(date)  # הדפסת התאריך
        count += 1

# ריצה של הפונקציה
print_millionth_date()
