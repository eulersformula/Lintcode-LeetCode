# Leetcode 1146//Medium//Apple

# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
# Constraints:

# 1 <= length <= 50000
# At most 50000 calls will be made to set, snap, and get.
# 0 <= index < length
# 0 <= snap_id < (the total number of times we call snap())
# 0 <= val <= 10^9

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.n_snaps = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.n_snaps:
            self.arr[index][-1] = (self.n_snaps, val)
        else:
            self.arr[index].append((self.n_snaps, val))
        
    def snap(self) -> int:
        self.n_snaps += 1
        return self.n_snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        if len(self.arr[index]) == 1:
            return self.arr[index][0][1]
        # 一开始未考虑情况：
        if self.arr[index][-1][0] <= snap_id:
            return self.arr[index][-1][1]
        st, ed = 0, len(self.arr[index]) - 1
        while st < ed - 1:
            mid = (st + ed) // 2
            if self.arr[index][mid][0] == snap_id:
                return self.arr[index][mid][1]
            if self.arr[index][mid][0] > snap_id:
                ed = mid # 一开始写成了ed = snap_id
            else:
                st = mid # 一开始写成了st = snap_id
        # 一开始二分法错误，没检查最后一个元素为snap_id的情况
        if self.arr[index][ed][0] == snap_id:
            return self.arr[index][ed][1]
        return self.arr[index][st][1]
        
