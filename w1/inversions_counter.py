def merge_and_count(x, y):
    """Merge two sorted arrays left, right and count inversions"""
    i, j, count = 0, 0, 0
    arr = []
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            arr.append(x[i])
            i += 1
        else:
            # when x[i] > y[j]
            # then x[i+1],...,x[n] also > y[j]
            count += len(x[i:])
            arr.append(y[j])
            j += 1

    if i < len(x):
        arr.extend(x[i:])
    else:
        arr.extend(y[j:])

    return count, arr

def sort_and_count(arr):
    if len(arr) == 1:
        return 0, arr

    mid = len(arr)/2
    left = arr[:mid]
    right = arr[mid:]

    count_left, sorted_left = sort_and_count(left)
    count_right, sorted_right = sort_and_count(right)
    count_split, sorted_total = merge_and_count(sorted_left, sorted_right)

    return count_left + count_right + count_split, sorted_total

def count(arr):
    return sort_and_count(arr)[0]

if __name__ == '__main__':
    with open("./w1/IntegerArray.txt", "r") as f:
        arr = f.readlines()
        arr = [int(i) for i in arr]
    print "The result is %s" % count(arr)
