def pathInZigZagTree(label):
        result = []
        level = 0
        node_count = 1
        while node_count * 2 <= label:
            node_count *= 2
            level += 1
        while label >= 1:
            result.append(label)
            level_start = 2 ** level
            level_end = 2 ** (level + 1) - 1
            label = (level_start + level_end - label) // 2
            level -= 1
        return result[::-1]

print(pathInZigZagTree(14))  # Output: [1, 3, 4, 14]
print(pathInZigZagTree(26))  # Output: [1, 2, 6, 10, 26]
