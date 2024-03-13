# Write your code here
def contains_duplicates(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return True

    return False 

print(contains_duplicates([1, 2, 3, 4, 4, 5, 6, 7]))
