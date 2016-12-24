"""Maximum weight independence set in a path graph
solving using dynamic programming"""

def mwis(arr):
    """arr: array of path weights
    return total weights of chosen path"""
    print "Arr: %s" % arr
    n = len(arr)

    w = [0] * (n+1)
    path = [0] * n

    w[1] = arr[0] # first vertex is chosen defautly
    path[0] = 1 # first vertex is chosen defautly

    for i in range(2, n+1):
        # without reconstructing the path
        w[i] = max(w[i-1], w[i-2] + arr[i-1])

    print "Weight: %s \n" % w[n]

    return w[n]
