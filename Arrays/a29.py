# find intersection of intervals

def intersection(arr1, arr2):
  i = j = 0
  n = len(arr1)
  m = len(arr2)
  while i < n and j < m:
    l = max(arr1[i][0], arr2[j][0])
    r = max(arr1[i][1], arr2[j][1])
    if l <= r:
      print("[" , l , "," , r , "]")
    if arr1[i][1] < arr2[j][1]:
      i += 1
    else:
      j += 1

arr1 = [ [ 0, 4 ], [ 5, 10 ],
         [ 13, 20 ], [ 24, 25 ] ]

arr2 = [ [ 1, 5 ], [ 8, 12 ], 
         [ 15, 24 ], [ 25, 26 ] ]

intersection(arr1, arr2)