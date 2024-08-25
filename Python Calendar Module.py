# """____Question: Calendar Module____"""


#-->A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format
    
import datetime

def find_day(date_str):
    month,day,year = map(int, [date_str[:2],[date_str[3:5],date_str[6:]]])    
    
    date = datetime.datetime(year,month,day)
    return date.strftime('%A')

date_str = input("enter: ")
print(find_day(date_str).upper())
