# Write your code here
def keys_with_value(dictionary, value):
    result = []
    for j, i in dictionary.items():
        if i == value:
           result += j
    return result