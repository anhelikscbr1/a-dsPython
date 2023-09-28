def bubble_sort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) -1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if(arr[min_idx] > arr[j]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while( j>=0 and arr[j+1] < arr[j]):
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j-=1
    print(arr)

arr = [3,5,8,0,-1,3,9, 10,4]
bubble_sort(arr)
selection_sort(arr)
insertion_sort(arr)