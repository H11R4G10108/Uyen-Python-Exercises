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

# Example usage:
date = "2019-01-09"
print(dayOfYear(date))  # Output: 9
date22 = "2019-02-10"
print(dayOfYear(date22))  # Output: 41
date23 = "2019-03-01"
print(dayOfYear(date23))  # Output: 60