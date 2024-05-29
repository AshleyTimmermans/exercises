# Write your code here
def double_dict_values(dictionary):
    result = {}
    for j, i in dictionary.items():
        x = i*2
        result[j] = x

    return result