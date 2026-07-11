arr = [7, 5 , 9 , 2 , 8]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1 , len(arr)):
        if arr[j] < arr [min_index]:
           min_index = j 
    if(min_index != i):
       swap = arr[i]
       arr[i] = arr[min_index]
       arr[min_index] = swap
print(arr)

def selection_sort(arr ,length, index):
    if(length == index):
        return arr
    min = index
    for i in range(index+1 , length):
        if arr[i] < arr[min]:
            min = i
    swap = arr[min]
    arr[min] = arr[index]
    arr[index] = swap
    return selection_sort(arr ,length,  index+1)
print(selection_sort(arr ,len(arr), 0))