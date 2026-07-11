arr = [7, 5 , 9 , 2 , 8]

def quick_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    p = arr[-1]
    l = [x for x in arr[:-1] if x <= p]
    r = [x for x in arr[:-1] if x > p]
    L = quick_sort(l)
    R = quick_sort(r)
    return L + [p] + R
print(quick_sort(arr))