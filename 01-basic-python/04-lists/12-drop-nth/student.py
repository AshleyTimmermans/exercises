# Write your code here
def drop_nth(xs, n):
    ys = xs[:n] + xs[n+1:]
    return ys

print(drop_nth([1,2,3,4, 5, 6], 3))

