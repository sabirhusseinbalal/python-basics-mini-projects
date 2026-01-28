from datetime import datetime
import calendar

# Step 1: Validate date
def is_valid_date(y, m, d):
    try:
        datetime(y, m, d)
        return True
    except ValueError:
        return False



    
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def age(cur_year, cur_month, cur_day):
    while True:
        print()
        bir_year = (input("Enter birth year: or Enter 'q' for Exist "))
        if bir_year.lower()=='q':
            print("...")
            break

        try:
            bir_year = int(bir_year)
        except ValueError:
            print("Please enter a valid year.")
            continue

        bir_month = int(input("Enter birth month: "))
        bir_day = int(input("Enter birth day: "))

        if is_valid_date(bir_year, bir_month, bir_day) == False:
            print("Invalid date. Try again.\n")
            continue

        # STEP 1 — YEARS
        year = cur_year - bir_year
        if (cur_month, cur_day) < (bir_month, bir_day):
            year -= 1

        # STEP 2 — MONTHS
        month = cur_month - bir_month
        if cur_day < bir_day:
            month -= 1
        if month < 0:
            month += 12

        # STEP 3 — DAYS
        if cur_day >= bir_day:
            day = cur_day - bir_day
        else:
            if cur_month == 1:
                prev_month = 12
                prev_year = cur_year - 1
            else:
                prev_month = cur_month - 1
                prev_year = cur_year

            days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
            day = days_in_prev_month - bir_day + cur_day

        
        if month > 0:
            print(f"Age: {year} years {month} months {day} days")
        else:
            print(f"Age: {year} years {day} days")

        # STEP 4 — TOTAL MONTHS
        total_months = (year*12)+month
        print(f"{total_months} months {day} days")

        # STEP 5 — TOTAL DAYS
        total_days = 0
        total_days = total_days + (calendar.monthrange(bir_year, bir_month)[1] - bir_day)
        for i in range(bir_month+1,13):
            total_days = total_days + calendar.monthrange(bir_year, i)[1]

        for i in range(bir_year+1,cur_year):
            if leap_year(i):
                total_days = total_days + 366
            else:
                total_days = total_days + 365

        if cur_month == 1:
            total_days = total_days + cur_day
        else:
            for i in range(1,cur_month):
                total_days = total_days + (calendar.monthrange(cur_year, i)[1])
            total_days = total_days + cur_day


        print(f"{total_days} days")


        # STEP 6 — TOTAL WEEKS
        weeks = total_days // 7
        extra_days = total_days % 7
        print(f"{weeks} weeks {extra_days} days")

        # STEP 7 — TOTAL HOURS
        hours = total_days * 24
        print(f"{hours} hours")

        # STEP 8 — TOTAL MINUTES
        minutes = hours * 60
        print(f"{minutes} minutes")

        # STEP 9 — TOTAL SECONDS
        seconds = minutes * 60
        print(f"{seconds} seconds")




# Today
today = datetime.today().date()


age(today.year, today.month, today.day) 
