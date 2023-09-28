def merge(arr1, arr2):
    i,j = 0,0
    arr = []
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    if(i == len(arr1)):
        arr = arr + arr2[j:]
    if(j == len(arr2)):
        arr = arr + arr1[i:]
    return arr

def merge_sort(arr):
    if(len(arr) < 2):
        return arr
    
    mid = (len(arr))//2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    return merge(arr1, arr2)

c = merge_sort([0,51,33,6,2, -1])
print(c)