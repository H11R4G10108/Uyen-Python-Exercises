def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False # negative numbers are not palindromes
        if x==0: return True # 0 is a palindrome
        str_x=str(x)
        reverse=str_x[::-1] # reverse the string
        if reverse==str_x:
            return True
        else:
            return False
        
# Test cases
print(isPalindrome(121))  # True
print(isPalindrome(-121)) # False
print(isPalindrome(10))   # False