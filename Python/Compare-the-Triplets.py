def compareTriplets(a, b):
    count = [0,0]
    for i in range(0,len(a)):
        if a[i] > b[i]:
            count[0] += 1
        elif a[i] < b[i]:
            count[1] += 1
    return count
