arr = [3,2,1]

def insertion_sort(arr, i ,n):
    if ( i == n):
        return arr
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1] , arr[j] = arr[j] , arr[j-1]
        j -= 1
    return insertion_sort(arr , i+1 , n)
print(insertion_sort(arr, 0, len(arr)))
for i in range(1 , len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = key
#print(arr)
            
            
        