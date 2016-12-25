
def knapsack(v, w, c):
    """v: array of values
        w: array of weights
        c: total weight capacity
        return optimal value of subset of items (1-n)"""

    n = len(v)
    # matrix of rows: items 1,2,..,n and columns: capacity 1,2,3...,C
    table = [[0] * (c+1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for x in range(c+1):
            if w[i-1] > x:
                table[i][x] = table[i-1][x]
            else:
                table[i][x] = max(table[i-1][x], table[i-1][x-w[i-1]] + v[i-1])

    return table[n][c]
