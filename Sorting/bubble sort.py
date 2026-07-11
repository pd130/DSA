
arr = [1,2,3]

def bubble_sort(arr, length):
    is_swap = False
    if length == 1:
        return arr
    for i in range(length-1):
        if arr[i] > arr[i+1]:
            swap = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = swap
            is_swap = True
    if not is_swap:
        return arr
    else:
        return bubble_sort(arr , length-1)
print(bubble_sort(arr , len(arr)))
    
    
for i in range(len(arr) - 1 , 0 , -1):
    is_swap = True
    for j in range(i):
        if arr[j] > arr[j+1]:
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
            is_swap = False
    if is_swap:
        print(arr)
        break
if not is_swap:
    #print(arr)
    pass
    
    
    
