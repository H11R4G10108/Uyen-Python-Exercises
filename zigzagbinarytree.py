"""Description: This function finds the path from the root to a given node in a zigzag binary tree.
A zigzag binary tree is a binary tree where the values of the nodes at each level are arranged in a zigzag pattern.

Input: A label of a node in a zigzag binary tree.
Output: The path from the root to the node with that label."""

"""ver1"""
def pathInZigZagTree(label):
    result=[]
    level=0
    node_count=1
    #calculate level of the label
    while node_count*2<= label:
        node_count*= 2
        level=level+1
    while label >=1:
        result.append(label)
        level_start=2**level #min num of the current level
        level_end=2**(level+1)-1 #max num of the current level
        label=(level_start+level_end-label)//2 #find the parent node
        level=level-1 #up we go to the parent level
    return result[::-1] #reverse the array

print(pathInZigZagTree(14))  # Output: [1, 3, 4, 14]
print(pathInZigZagTree(26))  # Output: [1, 2, 6, 10, 26]

"""Ver2"""
def pathInZigZagTree2(label):
    result=[]
    while label>=1:
        result.append(label)
        level=label.bit_length() - 1  #level starts from 0
        level_start=2**level #min num of the current level
        level_end=2**(level+1)-1 #max num of the current level
        #Convert to normal binary label, then move to parent, then back to zigzag
        label = (level_start + level_end - label) // 2
    return result[::-1]

print(pathInZigZagTree2(14))  # Output: [1, 3, 4, 14]
print(pathInZigZagTree2(26))  # Output: [1, 2, 6, 10, 26]
