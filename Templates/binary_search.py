# 左闭右开写法
def binary_search(arr, target):
  st, ed = 0, len(arr) # 退出条件st == ed
  while st < ed:
    mid = st + (ed - st) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      st = mid + 1
    else:
      ed = mid
  return -1

#左闭右闭写法
def binary_search(arr, target):
  st, ed = 0, len(arr)-1
  while st <= ed: # 退出条件st > ed
    mid = (st + ed) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      st = mid + 1
    else:
      ed = mid - 1
  return -1

# 相邻写法
def binary_search(arr, target):
  st, ed = 0, len(arr)-1 # 退出条件st == ed - 1
  while st < ed - 1:
    mid = (st + ed) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      st = mid
    else:
      ed = mid
if arr[st] == target:
  return st
if arr[ed] == target:
  return ed
return -1
