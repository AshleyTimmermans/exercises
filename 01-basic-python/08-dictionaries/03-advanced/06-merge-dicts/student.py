# Write your code here
def merge_dicts(dict1, dict2):
    merged_dict = {}
    for i, j in dict2.items():
        merged_dict[i] = j
    for x, y in dict1.items():
        if x not in merged_dict:
            merged_dict[x] = y
    return merged_dict
