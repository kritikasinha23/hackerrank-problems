def miniMaxSum(arr):
    max_num = max(arr)
    min_num = min(arr)
    SumOfArray = 0
    if len(arr) == 5:
        for i in arr:
            SumOfArray += i
        print((SumOfArray - max_num), (SumOfArray - min_num))
