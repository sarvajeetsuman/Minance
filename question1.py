"""
Question 1:
Write a program to take the year as the input from the user. 
If the current year is a leap year then print the day of the extra day in the year.
If the entered year is not a leap year, find the closest leap year either before or after the current year and then print the day of the extra day in the year. 

Exception case:
If the closest leap year either before or after is equidistant from the current year, print the day of the extra day in the year in both cases 

Sample1:
Input: 2012
Output:
Wednesday

Sample2:
Input: 2013
Output:
This is not a leap year
Closest leap year: 2012
Wednesday

"""

import datetime

def find_day(num):
    """ Returns day """
    lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return lst[num]

def find_date(year):
    """ creates date & calls find_day to get Day"""
    dateobj = datetime.date(year, 2, 29)
    num = dateobj.weekday()
    return find_day(num)

def find_leap_year(year):
    """ Finds Closest Leap Year"""
    if year%100==0 and year%400 != 0:
        year1 = year+4
        year2 = year-4
        print("year {} is a leap year".format(year1))
        print("year {} is a leap year".format(year2))
        print(find_date(year1))
        print(find_date(year2))
    else:
        if year%4 >2:
            year = year + (4-year%4)
            if year%100==0 and year%400 != 0:
                year = year - 4
            print("year {} is a leap year".format(year))
            print(find_date(year))
        elif year%4 < 2:
            year = year - (year%4)
            if year%100==0 and year%400 != 0:
                year = year + 4
            print("year {} is a leap year".format(year))
            print(find_date(year))
        else:
            flag1 = False
            flag2 = False
            year1 = year - 2
            year2 = year + 2
            if year%100==0 and year%400 != 0:
                flag1 = True
            if year%100==0 and year%400 != 0:
                flag2 = True 
            if flag1 == False and flag2 == False:
                print("Leap year is equidistant from given year")
                print("So two leap years are {0} and {1}".format(year1, year2))
                print(find_date(year1))
                print(find_date(year2))
            elif flag1 == True:
                print("year {} is a leap year".format(year2))
                print(find_date(year2))
            elif flag2 == True:
                print("year {} is a leap year".format(year1))
                print(find_date(year1))

def check_leap_year(year):
    """ Checks Leap Year"""
    if year%100==0 and year%400 != 0:
        print("year {} is not a leap year".format(year))
        find_leap_year(year)
    else:
        if year%4 == 0:
            print("year {} is leap year".format(year))
            print(find_date(year))
        else:
            print("year {} is not a leap year".format(year))
            find_leap_year(year)



if __name__ == '__main__':
     year = int(input())
     check_leap_year(year)