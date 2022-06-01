# Lintcode 1070//Medium//Facebook
# Description
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

# Example
# Example 1:
# 	Input:
# 	[
# 		["John", "johnsmith@mail.com", "john00@mail.com"],
# 		["John", "johnnybravo@mail.com"],
# 		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
# 		["Mary", "mary@mail.com"]
# 	]
	
# 	Output: 
# 	[
# 		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# 		["John", "johnnybravo@mail.com"],
# 		["Mary", "mary@mail.com"]
# 	]

# 	Explanation: 
# 	The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# 	The second John and Mary are different people as none of their email addresses are used by other accounts.

# 	You could return these lists in any order, for example the answer
	
# 	[
# 		['Mary', 'mary@mail.com'],
# 		['John', 'johnnybravo@mail.com'],
# 		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
# 	]
# 	is also acceptable.

from typing import (
    List,
)

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n_clusters = n
    
    def find(self, i: int) -> int:
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while i != root:
            tmp = self.parent[i]
            self.parent[i] = root
            i = tmp
        return root
    
    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] >= self.size[root_j]:
                self.parent[root_j] = root_i
                self.size[i] += self.size[root_j]
            else:
                self.parent[root_i] = root_j
                self.size[j] += self.size[root_i]
            self.n_clusters -= 1

class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
             we will sort your return value in output
    """
    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        # write your code here
        # Questions to ask:
        # 1. Is it possible for the same email to have different names?
        email_sets = []
        n_accounts = len(accounts)
        for account in accounts:
            emails = set(account[1:])
            email_sets.append(emails)
        union_find = UnionFind(n_accounts)
        for i in range(n_accounts-1):
            for j in range(i+1, n_accounts):
                if len(email_sets[i] & email_sets[j]) > 0:
                    union_find.union(i, j)
        clusters = dict()
        for i in range(n_accounts):
            root_i = union_find.find(i)
            if root_i not in clusters:
                clusters[root_i] = set()
            clusters[root_i] |= email_sets[i]
        res = []
        for c, emails in clusters.items():
            res.append([accounts[c][0]] + sorted(list(emails)))
        return res

# 网上找的非常好的答案及复杂度分析

# 哈希表 + 并查集
# 两个账户需要合并，当且仅当两个账户至少有一个共同的邮箱地址，因此这道题的实质是判断所有的邮箱地址中有哪些邮箱地址必定属于同一人，可以使用并查集实现。

# 为了使用并查集实现账户合并，需要知道一共有多少个不同的邮箱地址，以及每个邮箱对应的名称，因此需要使用两个哈希表分别记录每个邮箱对应的编号和每个邮箱对应的名称，遍历所有的账户并在两个哈希表中记录相应的信息。虽然同一个邮箱地址可能在多个账户中出现，但是同一个邮箱地址在两个哈希表中都只能存储一次。

# 然后使用并查集进行合并操作。由于同一个账户中的邮箱地址一定属于同一个人，因此遍历每个账户，对账户中的邮箱地址进行合并操作。并查集存储的是每个邮箱地址对应的编号，合并操作也是针对编号进行合并。

# 完成并查集的合并操作之后，即可知道合并后有多少个不同的账户。遍历所有的邮箱地址，对于每个邮箱地址，通过并查集得到该邮箱地址属于哪个合并后的账户，即可整理出每个合并后的账户包含哪些邮箱地址。

# 对于每个合并后的账户，需要整理出题目要求的返回账户的格式，具体做法是：将邮箱地址排序，账户的名称可以通过在哈希表中查找任意一个邮箱对应的名称得到，将名称和排序后的邮箱地址整理成一个账户列表。对所有合并后的账户整理出账户列表，即可得到最终答案。

from typing import (
    List,
)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

class Solution:
    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        uf = UnionFind(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, emailToIndex[email])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)
        
        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans

# 时间复杂度：O(nlogn)，其中 n 是不同邮箱地址的数量。
# 需要遍历所有邮箱地址，在并查集内进行查找和合并操作，对于两个不同的邮箱地址，如果它们的祖先不同则需要进行合并，需要进行 2 次查找和最多 1 次合并。一共需要进行 2n 次查找和最多 nn 次合并，因此时间复杂度是 O(2n \log n)=O(n \log n)O(2nlogn)=O(nlogn)。这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 O(n \log n)O(nlogn)，平均情况下的时间复杂度依然是 O(n \alpha (n))O(nα(n))，其中 \alphaα 为阿克曼函数的反函数，\alpha (n)α(n) 可以认为是一个很小的常数。
# 整理出题目要求的返回账户的格式时需要对邮箱地址排序，时间复杂度是 O(nlogn)。
# 其余操作包括遍历所有邮箱地址，在哈希表中记录相应的信息，时间复杂度是 O(n)，在渐进意义下 O(n) 小于 O(nlogn)。
# 因此总时间复杂度是 O(nlogn)。

# 空间复杂度：O(n)，其中 n 是不同邮箱地址的数量。空间复杂度主要取决于哈希表和并查集，每个哈希表存储的邮箱地址的数量为 n，并查集的大小为 n。
