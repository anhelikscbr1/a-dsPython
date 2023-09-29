arr = [1,2,5,7,9,78,399]
target = 3
l, r = 0, len(arr) - 1

while (l <= r):
    m = (l + r) // 2
    print(m)
    if(arr[m] > target):
        r = m - 1
    if(arr[m] < target):
        l = m + 1
    if(arr[m] == target):
        print(m) 
        break