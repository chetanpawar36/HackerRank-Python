# """____Question: Leap Year____"""


#-->Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.



def is_leap(year):
    
    if year % 4 == 0:
        
        if year % 100 == 0:
            
            if year % 400 == 0:    
                return True
            
            else:
                return False
        
        else:
            return True
    
    else:
        return False
    
year = int(input("enter the year to analyze(leap year): "))
print(is_leap(year))
