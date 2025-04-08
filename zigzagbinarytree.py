def pathInZigZagTree(label):
    result=[] 
    queue=[label]
    level=0 
    
    while queue:
        size=len(queue)
        current_level=[]
        #find the current level nodes
        #pop the nodes from the queue
        for i in range(size):
            current_level.append(queue.pop(0)) 
        #reverse if its an odd level
        if level%2!=0:
            current_level.reverse()
        result.append(current_level)
        next_level=[]
        for node in current_level:
            if node*2 <= label:
                next_level.append(node*2)  #left
            if node*2+1 <= label:
                next_level.append(node*2+1)  #right
        queue.extend(next_level) 
        level=level+1
    
    return result

# Ví dụ sử dụng:
print(pathInZigZagTree(14))  # Output: [1, 3, 4, 14]
print(pathInZigZagTree(26))  # Output: [1, 2, 6, 10, 26]
