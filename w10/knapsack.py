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

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def knapsack_re(v, w, c):
    """knapsack recursive top-down approach
    only compute needed subproblems
    for problem with huge data"""
    n = len(v)

    @Memoize
    def table(i, x):
        if i == 0: return 0

        if w[i-1] > x:
            return table(i-1, x)
        else:
            return max(table(i-1, x), table(i-1, x-w[i-1]) + v[i-1])

    return table(n, c)

if __name__ == "__main__":
    with open("w10/knapsack_big.txt") as f:
        c, _ = map(int, next(f).split())
        items = [map(int, line.split()) for line in f]

    v, w = zip(*items)
    print knapsack_re(v, w, c)
