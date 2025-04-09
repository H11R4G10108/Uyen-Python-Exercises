"""Description: find the day of the year for the given date
Input: A date string
Output: interger representing the day of the year
"""

"""Ver1"""
def dayOfYear(date):
        hashmap={
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
            } 
        year=int(date[0:4]) 
        month=int(date[5:7])
        day=int(date[8:10])
        dayneeded=0 
        if month==1:  
            dayneeded=day 
            return dayneeded
        else:
            if year%4==0 and year%100!=0 or year%400==0:    
                hashmap[2]=29
            dayneeded=day
            for i in range(1,month):
                dayneeded=dayneeded+int(hashmap[i])
        return dayneeded

date = "2019-01-09"
print(dayOfYear(date))  # Output: 9
date22 = "2019-02-10"
print(dayOfYear(date22))  # Output: 41
date23 = "2019-03-01"
print(dayOfYear(date23))  # Output: 60

"""Ver2"""
def dayOfYear2(date):
    year, month, day = map(int, date.split('-'))
    months = [0, 31, 59 ,90, 120, 151, 181, 212, 243, 273, 304, 334] #list of days in a year when a specific month ends
    if month > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)): #check leaps year only when the date is past feb
        day+=1
    return months[month - 1] + day

date1 = "2019-01-09"
print(dayOfYear2(date1))  # Output: 9
date22 = "2019-02-10"
print(dayOfYear2(date22))  # Output: 41
date23 = "2019-03-01"
print(dayOfYear2(date23))  # Output: 60
