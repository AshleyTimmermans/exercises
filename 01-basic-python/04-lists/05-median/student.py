# Write your code here
def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 0:
        under = (len(ns)-1)// 2
        upper = (len(ns)+1) // 2 
        median = (ns[under] + ns[upper])/2
    else:
        median = len(ns) // 2

    return median


print(median([1, 2, 3, 4]))

