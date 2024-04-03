import itertools


# answer = ['A', 'B', 'C', 'D']
# permutations = [''.join(p) for p in itertools.product(answer, repeat=10)]
# print(len(permutations))

def char_frequency_difference(s):
    # 统计每个字符的出现次数
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

        # 找出出现次数最多的字符及其次数
    max_count = max(char_counts.values())

    # 找出出现次数最少的字符及其次数（排除未出现的字符）
    min_count = min(count for count in char_counts.values() if count > 0)

    # 计算差值
    difference = max_count - min_count
    return difference


s = 'ABBBCCCDDDD'
print(char_frequency_difference(s))
