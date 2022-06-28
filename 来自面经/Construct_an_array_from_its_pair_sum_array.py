# Medium
# https://www.geeksforgeeks.org/construct-array-pair-sum-array/

# Given a pair-sum array and size of the original array (n), construct the original array.
# A pair-sum array for an array is the array that contains sum of all pairs in ordered form. For example pair-sum array for arr[] = {6, 8, 3, 4} is {14, 9, 10, 11, 12, 7}.
# In general, pair-sum array for arr[0..n-1] is {arr[0]+arr[1], arr[0]+arr[2], ..., arr[1]+arr[2], arr[1]+arr[3], ..., arr[2]+arr[3], arr[2]+arr[4], ..., arr[n-2]+arr[n-1}.

# 一开始想的麻烦做法
from typing import List
def findOriginalArray(n: int, pair_sum: List[int]) -> List[int]:
    # a[0]+a[1], a[0]+a[2], ..., a[0]+a[n-1] s_0 = (n-1) * a[0] + (a[1] + a[2] + ... + a[n-1])
    # a[1]+a[2], a[1]+a[3], ..., a[1]+a[n-1] s_1 = (n-2) * a[1] + (a[2] + a[3] + ... + a[n-1])
    # a[2]+a[3], a[2]+a[4], ..., a[2]+a[n-1] s_2 = (n-3) * a[2] + (a[3] + a[4] + ... + a[n-1])
    # s_0 - s_1 = (n-1) * a[0] - (n-3) * a[1]
    # s_1 - s_2 = (n-2) * a[1] - (n-4) * a[2]
    # s_2 - s_3 = (n-3) * a[2] - (n-5) * a[3] 
    # (n-k-3) * a[k] + (n-k-3) * a[k+1] = (n-k-3) * p
    # (n-k-1) * a[k] - (n-k-3) * a[k+1] = q
    # a[k] = ((n-k-3) * p + q) // (2n-2k-4)
    # store pair_sum[0], pair_sum[n-1], pair_sum[n-1 + n-2]
    # For n = 4:
    # a[0]+a[1] (0), a[0]+a[2] (1), a[0]+a[3] (2) p = a[0] + a[1]; q = 3a[0] - a[1]; a[0] = (p+q) // 4
    # a[1]+a[2] (3), a[1]+a[3] (4)
    # a[2]+a[3] (5)
    idx, tmp_0, tmp_1, k = 0, [], [], 1
    while idx < len(pair_sum):
        tmp_0.append(pair_sum[idx])
        tmp_1.append(sum(pair_sum[idx:(idx+n-k)]))
        idx += n - k
        k += 1
    print(tmp_0, tmp_1)
    res = []
    for idx in range(len(tmp_0)-1):
        p = tmp_0[idx]
        q = tmp_1[idx] - tmp_1[idx+1]
        cur = ((n-idx-3)*p+q) // (2*n-2*idx-4)
        res.append(cur)
    v = pair_sum[-2] - res[-1]
    w = pair_sum[-1] - v
    res.append(w)
    res.append(v)
    return res

# 简单做法: T: O(n); S: O(1)
def findOriginalArray(n: int, pair_sum: List[int]) -> List[int]:
    # a[0]+a[1], a[0]+a[2], ..., a[0]+a[n-1] 
    # a[1]+a[2], a[1]+a[3], ..., a[1]+a[n-1] 
    # a[2]+a[3], a[2]+a[4], ..., a[2]+a[n-1] 
    # a[0] = (pair_sum[0] + pair_sum[1] - pair_sum[n-1]) // 2
    # a[1] = (pair_sum[n-1] + pair_sum[n] - pair_sum[2n-5]) // 2
    # n = 4, 6 pairs
    # 0, 1, 3
    # 3, 4, 5
    
    res = []
    idx, k = 0, 1
    while idx < len(pair_sum)-1:
        cur = (pair_sum[idx] + pair_sum[idx+1] - pair_sum[idx+n-k]) // 2
        res.append(cur)
        idx += n - k
        k += 1
    last = pair_sum[n-2] - res[0]
    res.append(pair_sum[-1] - last)
    res.append(last)
    return res
    

# findOriginalArray(4, [14, 9, 10, 11, 12, 7]) -> [6, 8, 3, 4]
