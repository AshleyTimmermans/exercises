# Write your code here
def sum_dict_values(dictionary):
    sum = 0
    for i in iter(dictionary.values()):
        sum += i
    return sum
