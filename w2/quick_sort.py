T = 3 # t: type of choosing rule (1,2,3)

def choose_pivot(arr, begin, end):
    """Choose pivot
        swap the choosen one to the 1st place
        of the sub array (begin index)
    """
    if T == 1:
        # always choose first element
        return
    elif T == 2:
        # always choose final element
        arr[begin], arr[end] = arr[end], arr[begin]
        return

    # choose by "median of three" rule
    first = arr[begin]
    last = arr[end]
    half = begin + (end-begin)/2
    mid = arr[half]
    if first <= mid <= last or last <= mid <= first:
        arr[begin], arr[half] = arr[half], arr[begin]
    elif mid <= last <= first or first <= last <= mid:
        arr[begin], arr[end] = arr[end], arr[begin]

    return

def partition(arr, begin, end):
    """Swap elements in arr
        with pivot is the first element so that
        left < pivot < right elements
        return index of pivot after partitioned
    """
    i = begin
    p = arr[begin]
    for j in range(begin+1, end+1):
        if arr[j] < p:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
    arr[i], arr[begin] = arr[begin], arr[i]
    return i

def quick_sort(arr, begin=0, end=None, c=None):
    if end is None:
        end = len(arr) - 1

    if end <= begin:
        return

    # excercises: count number of comparisons
    if c is None:
        c = [len(arr)-1,]
    else:
        c[0] += (end - begin)

    choose_pivot(arr, begin, end)
    p = partition(arr, begin, end)
    quick_sort(arr, begin, p-1, c)
    quick_sort(arr, p+1, end, c)

    return c

if __name__ == "__main__":
    with open("QuickSort.txt", "r") as f:
        arr = f.readlines()
        arr = [int(i) for i in arr]
    c = quick_sort(arr)
    print c
