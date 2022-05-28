# Lintcode 1900//Hard//Google

# Description
# Given two gene fragment Gene1 and Gene2, the gene fragment is composed of numbers and four characters: "ACGT".
# Each character is preceded by a corresponding number, which describes the number of consecutive occurrences of the character. For example, "1A2C2G1T" means "ACCGGT".
# Return a string which denote the similarity of two gene fragments.
# The definition of similarity string is that "the number of characters equal in the same position" + "/" + "the total number of characters".

# Gene1 and Gene2 only contain ["A", "C", "G", "T"] and digit.
# The length of Gene1 and Gene2 is within range: [1, 100000]
# The count of characters is within range: [1, 10000000]
# Guarantee the length of Gene1 and Gene2 by expansion are equal.
# Example
# Example 1:
# Input:
# Gene1: "2T3G"
# Gene2: "3T2G"
# Output: 
# "4/5"
# Explanation: 
# "TTTGG" and "TTGGG" have 4 position same gene, so "4/5"
# Example 2:
# Input:
# Gene1 = "3T2G4A1C"
# Gene2 = "6T1A2C1G"
# Output: 
# "4/10"
# Explanation: 
# "TTTGGAAAAC" and "TTTTTTACCG" hava 4 position gene same, so "4/10"

# SOLUTION 1: T: O(N); S: O(N); N is the expanded length of gene. TIME LIMIT EXCEEDED.

class Solution:
    """
    @param gene1: a string
    @param gene2: a string
    @return: return the similarity of two gene fragments
    """
    def gene_similarity(self, gene1: str, gene2: str) -> str:
        # write your code here
        # Questions to ask:
        # 1. Is it possible that the len of gene is 0?
        # 2. Is it guaranteed that the two genes have the same len?
        # 最一开始未考虑情况：可以是多位数
        gene1_full = ''
        st, ed, num = 0, 0, ''
        while ed < len(gene1):
            while gene1[ed] >= '0' and gene1[ed] <= '9':
                ed += 1
            n, l = int(gene1[st:ed]), gene1[ed]
            gene1_full += l * n
            st = ed + 1
            ed = st
        gene2_full = ''
        st, ed, num = 0, 0, ''
        while ed < len(gene2):
            while gene2[ed] >= '0' and gene2[ed] <= '9':
                ed += 1
            n, l = int(gene2[st:ed]), gene2[ed]
            gene2_full += l * n
            st = ed + 1
            ed = st
        same = 0
        for i in range(len(gene1_full)): # 最开始把gene1_full写成了gene1
            if gene1_full[i] == gene2_full[i]:
                same += 1
        # equivalently 
        # same = sum([1 for l1, l2 in zip(gene1_full, gene2_full) if l1 == l2 else 0])
        return str(same) + '/' + str(len(gene1_full))

# SOLUTION 2:
class Solution:
    """
    @param gene1: a string
    @param gene2: a string
    @return: return the similarity of two gene fragments
    """
    # 改善：一开始就parse出所有的segments存在数组里
    from typing import Tuple
    def get_next_num_char(self, gene: str, idx: int) \
                          -> Tuple[int, int, str]:
        num_ed = idx + 1
        while gene[num_ed] >= '0' and gene[num_ed] <= '9' and \
              num_ed < len(gene):
            num_ed += 1
        return (num_ed+1, int(gene[idx:num_ed]), gene[num_ed])

    def gene_similarity(self, gene1: str, gene2: str) -> str:
        # write your code here
        # Questions to ask:
        # 1. Is it possible that the len of gene is 0?
        # 2. Is it guaranteed that the two genes have the same len?
        # 最一开始未考虑情况：可以是多位数
        if len(gene1) == 0:
            return '0/0'
        idx_1, idx_2, n_1, n_2, char_1, char_2 = 0, 0, 0, 0, '', ''
        n_same, n_chars = 0, 0
        while not(idx_1 == len(gene1) and idx_2 == len(gene2) and \
                  n_1 == 0 and n_2 == 0): # 一开始循环结束条件写错
            if n_1 == 0:
                idx_1, n_1, char_1 = self.get_next_num_char(gene1, idx_1)
            elif n_2 == 0:
                idx_2, n_2, char_2 = self.get_next_num_char(gene2, idx_2)
            else:
                to_del = min(n_1, n_2)
                n_chars += to_del
                if char_1 == char_2:
                    n_same += to_del
                n_1 -= to_del
                n_2 -= to_del
            # print(idx_1, n_1, char_1, idx_2, n_2, char_2, n_same, n_chars)
        return str(n_same) + '/' + str(n_chars)
      
