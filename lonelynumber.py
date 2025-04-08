#Description: Given an integer array nums, return all the lonely numbers in the array. 
# A lonely number is a number that appears exactly once in the array and does not have any adjacent numbers (i.e., its value minus 1 and its value plus 1) in the array.
#Input: an integer array nums
#Ouput: an integer array of lonely numbers

def findLonely(nums):
        list_lonely=[] 
        num_status={} #a hashmap to store the numer and its status
        for i in nums:
            if i in num_status: #if it appears again its status gets changed
                #status -1: not lonely number
                num_status[i]=-1
            else:
                num_status[i]=1
            num_status[i+1]=-1 #add its next number to make sure the next one is also not lonely
            num_status[i-1]=-1
        for i in nums:
            if num_status[i]==1: #check the status
                list_lonely.append(i)
        return list_lonely

print(findLonely([10,6,5,8])) # [10,8]
print(findLonely([1,3,5,3])) # [1,5]