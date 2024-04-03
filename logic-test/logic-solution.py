import itertools


class LogicSolution:

    def getResult(self) -> str:
        answer = ['A', 'B', 'C', 'D']
        permutations = [''.join(p) for p in itertools.product(answer, repeat=10)]
        for permutation in permutations:
            if self.judge_all(permutation):
                return permutation
        return ''

    def judge_all(self, p: str) -> bool:
        return self.judge_q2(p) and self.judge_q3(p) and self.judge_q4(p) and self.judge_q5(p) and self.judge_q6(
            p) and self.judge_q7(p) and self.judge_q8(p) and self.judge_q9(p) and self.judge_q10(p)

    def judge_q2(self, p: str) -> bool:
        if p[1] == 'A' and p[4] == 'C': return True
        if p[1] == 'B' and p[4] == 'D': return True
        if p[1] == 'C' and p[4] == 'A': return True
        if p[1] == 'D' and p[4] == 'B': return True
        return False

    def judge_q3(self, p: str) -> bool:
        if p[2] != p[5] and p[5] == p[1] and p[5] == p[3] and p[2] == 'A': return True
        if p[5] != p[2] and p[2] == p[1] and p[2] == p[3] and p[2] == 'B': return True
        if p[1] != p[2] and p[2] == p[5] and p[2] == p[3] and p[2] == 'C': return True
        if p[3] != p[2] and p[2] == p[5] and p[2] == p[1] and p[2] == 'D': return True
        return False

    def judge_q4(self, p: str) -> bool:
        if p[0] == p[4] and p[3] == 'A': return True
        if p[1] == p[6] and p[3] == 'B': return True
        if p[0] == p[8] and p[3] == 'C': return True
        if p[5] == p[9] and p[3] == 'D': return True
        return False

    def judge_q5(self, p: str) -> bool:
        if p[4] == 'A' and p[7] == 'A': return True
        if p[4] == 'B' and p[3] == 'B': return True
        if p[4] == 'C' and p[8] == 'C': return True
        if p[4] == 'D' and p[6] == 'D': return True
        return False

    def judge_q6(self, p: str) -> bool:
        if p[1] == p[3] and p[1] == p[7] and p[5] == 'A': return True
        if p[0] == p[5] and p[0] == p[7] and p[5] == 'B': return True
        if p[2] == p[9] and p[2] == p[7] and p[5] == 'C': return True
        if p[4] == p[8] and p[4] == p[7] and p[5] == 'D': return True
        return False

    def judge_q7(self, p: str) -> bool:
        min_val = self.find_least_frequent_char(p)
        if p[6] == 'A' and min_val == 'C': return True
        if p[6] == 'B' and min_val == 'B': return True
        if p[6] == 'C' and min_val == 'A': return True
        if p[6] == 'D' and min_val == 'D': return True
        return False

    def judge_q8(self, p: str) -> bool:
        if (self.is_adjacent(p[6], p[0]) is False) and p[7] == 'A': return True
        if (self.is_adjacent(p[5], p[0]) is False) and p[7] == 'B': return True
        if (self.is_adjacent(p[1], p[0]) is False) and p[7] == 'C': return True
        if (self.is_adjacent(p[9], p[0]) is False) and p[7] == 'D': return True
        return False

    def judge_q9(self, p: str) -> bool:
        if p[0] == p[5]:
            if p[5] != p[4] and p[8] == 'A': return True
            if p[9] != p[4] and p[8] == 'B': return True
            if p[1] != p[4] and p[8] == 'C': return True
            if p[8] != p[4] and p[8] == 'D': return True
        else:
            if p[5] == p[4] and p[8] == 'A': return True
            if p[9] == p[4] and p[8] == 'B': return True
            if p[1] == p[4] and p[8] == 'C': return True
            if p[8] == p[4] and p[8] == 'D': return True
        return False

    def judge_q10(self, p: str) -> bool:
        reduce = self.char_frequency_difference(p)
        if reduce == 3 and p[9] == 'A': return True
        if reduce == 2 and p[9] == 'B': return True
        if reduce == 4 and p[9] == 'C': return True
        if reduce == 1 and p[9] == 'D': return True
        return False

    def is_adjacent(self, p1: str, p2: str) -> bool:
        adjacent_chars = {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['C']
        }
        return p2 in adjacent_chars.get(p1, []) or p1 in adjacent_chars.get(p2, [])

    def find_least_frequent_char(self, s):
        # 初始化一个字典来存储每个字符的出现次数
        char_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        # 统计每个字符的出现次数
        for char in s:
            if char in char_counts:
                char_counts[char] += 1

                # 找出出现次数最少的字符及其次数
        return min(char_counts, key=char_counts.get)

    def char_frequency_difference(self, s: str) -> int:
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


solution = LogicSolution()
print(solution.getResult())  # BCACACDABA
