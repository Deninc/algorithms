"""Maximum weight independence set in a path graph
solving using dynamic programming"""

def mwis(arr):
    """arr: array of path weights
    return total weights of chosen path"""
    print "Arr: %s" % arr
    n = len(arr)

    w = [0] * (n+1)
    w[1] = arr[0] # first vertex is chosen defautly

    for i in range(2, n+1):
        w[i] = max(w[i-1], w[i-2] + arr[i-1])

    # reconstruct the path
    path = []
    i = n
    while i > 0:
        if w[i] != w[i-1]:
            path.append(arr[i-1])
            i -= 2
        else:
            i -= 1

    path.reverse()
    print "Path: %s" % path
    print "Weight: %s \n" % w[n]

    return w[n]
