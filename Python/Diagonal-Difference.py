def diagonalDifference(arr):
    pri_d = 0
    sec_d = 0
    for i in range(len(arr)):
        pri_d += arr[i][i]
        sec_d += arr[i][len(arr)-i-1]
    return abs(pri_d - sec_d)
        
