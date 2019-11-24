#Code by Infiltrat8r

##A program for calculating number of days between two dates.

from datetime import date 

try :
    print('\n\n\nThis program calculates the number of days Between two given dates')
    
    date_1_year = int(input('\n\n\nEnter the Year for the first date: '))
    date_1_month = int(input('Enter the Month for the first date: '))
    date_1_day = int(input('Enter the Date for the first date: '))
    
    date_2_year = int(input('Enter the Year for the Second date: '))
    date_2_month = int(input('Enter the Month for the Second date: '))
    date_2_day = int(input('Enter the Day for the Second date: '))
    
    date_1 = date(date_1_year, date_1_month, date_1_day)
    date_2 = date(date_2_year, date_2_month, date_2_day)
    
    days_between = date_1 - date_2
    diffrence = days_between.days
    print('\n\n\nThere is a diffrence of',abs(diffrence),'Days between',date_1,date_2)
    
except:
    print('There is an error in the format you inputed the dates.\nThis program only accepts integers :) ')


#for refence on how to use the date time library in python visit
##(https://www.w3schools.com/python/python_datetime.asp)
