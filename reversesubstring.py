#Description: Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#Input: a string that consists of lower case English letters and brackets.
#Output: a reversed string 

def reverseParentheses(s):
    stack=[]
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop()) #pop will return the character we remove, so when we append it to temp, we are reversing the order of the characters
            stack.pop() #pop the open bracket
            # Now we need to add the reversed characters back to the stack
            stack.extend(temp) 
        else:
            stack.append(char) #add character to the stack until we reach a close bracket
    return ''.join(stack)


# Example usage
s = "(u(love)i)"
print(reverseParentheses(s))  # Output: "iloveu"
    
s11 = "(ed(et(oc))el)"
print(reverseParentheses(s11))  # Output: "leetcode"
    
s2 = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s2))  # Output: "apmnolkjihgfdcbq"