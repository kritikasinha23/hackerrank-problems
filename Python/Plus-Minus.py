def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1    
        elif arr[i] == 0:
            z += 1           
    pos = p/len(arr)
    neg = n/len(arr)
    zero = z/len(arr)
    print("%.6f" %pos)
    print("%.6f" %neg)
    print("%.6f" %zero)
