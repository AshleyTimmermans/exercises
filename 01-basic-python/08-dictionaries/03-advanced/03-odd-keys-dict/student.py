# Write your code here
def odd_keys_dict(dictionary):
    odd = {}
    for j, i in dictionary.items():
        if j % 2 != 0:
            odd[j] = i
    return odd
