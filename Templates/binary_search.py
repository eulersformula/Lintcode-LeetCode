def binary_search(arr, target):
  if len(arr) == 0:
    return None
  st, ed = 0, len(arr)
  while st < ed:
    mid = (st + ed) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      st = mid
    else:
      ed = mid
  return -1
