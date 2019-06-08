
def is_leap():
    Year = int(input('enter a year: '))
    
    if len(str(Year)) <= 3 or len(str(Year)) > 4 :
        print Year,': Please enter a 4 digit number'
    
    elif Year % 4 == 0 or Year %400 == 0:
        print Year,'is a leap year'
        return True
        
    else:
        print Year, 'is not a leap year'
        return False
    return Year
is_leap()
# print(is_leap(2014))
# print(is_leap(2000))
# print(is_leap(124))
# print(is_leap(2008))
# print(is_leap(2010))
# print(is_leap(18844))