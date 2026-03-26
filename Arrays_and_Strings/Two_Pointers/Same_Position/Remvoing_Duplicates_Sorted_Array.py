# Removing Duplicated from Sorted Array using Two Pointers Same Direction

def removing_duplicates_sorted_Array(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

arr = list(map(int,input().split()))
result = removing_duplicates_sorted_Array(arr)
print(arr[:result])