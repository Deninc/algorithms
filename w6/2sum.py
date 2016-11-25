"""2SUM algorithm"""

def find_pair(arr, s, t):
    """return true if there is pair x,y, x!=y
    in set s / arr that x+y=t"""
    for x in arr:
        y = t-x
        if (y in s) and (x != y):
            return True
    return False

# if __name__ == "__main__":
#     with open("./w6/2sum.txt") as f:
#         l = f.readlines()
#     print "Done read file"
#     l = map(int, l)
#     s = set(l)
#     count = 0
#     r = range(-10000, 10001)
#     print "Start couting"
#     for t in r:
#         print t
#         if find_pair(l, s, t):
#             count += 1
#     print count
