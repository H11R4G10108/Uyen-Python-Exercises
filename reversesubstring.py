"""Description: Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Input: a string that consists of lower case English letters and brackets.
Output: a reversed string 
"""

"""ver1"""
def reverseParentheses(s):
    stack=[]
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(': #the last character in the stack is not an open bracket
                temp.append(stack.pop())
            #pop will return the character we remove, so when we append it to temp, we are reversing the order of the characters
            stack.pop() #pop the open bracket
            # Now we need to add the reversed characters back to the stack
            stack.extend(temp) 
        else:
            stack.append(char) #add character to the stack until we reach a close bracket
    return ''.join(stack)

s = "(u(love)i)"
print(reverseParentheses(s))  # Output: "iloveu"
    
s11 = "(ed(et(oc))el)"
print(reverseParentheses(s11))  # Output: "leetcode"
    
s2 = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s2))  # Output: "apmnolkjihgfdcbq"

"""ver2"""
def reverseParentheses2(s):
    stack = []
    s = list(s)
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i) #append the indices of the parentheses
        elif char == ')':
            #j is the index of the last open bracket and i is the index of the corresponding close bracket
            j = stack.pop() 
            s[j+1:i] = s[j+1:i][::-1] #reverse that part of the list
    return ''.join(char for char in s if char not in '()')

s = "(u(love)i)"
print(reverseParentheses2(s))  # Output: "iloveu"
    
s11 = "(ed(et(oc))el)"
print(reverseParentheses2(s11))  # Output: "leetcode"
    
s2 = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s2))  # Output: "apmnolkjihgfdcbq"
