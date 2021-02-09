#!/usr/local/bin python3
from pprint import pprint
def sum_list(arr):
    if arr == []:
        return 0
    return arr[0] + sum_list(arr[1:])


arr = ['this', 'is', 'my', 'list']
nums = [1, 2, 3, 4]

print(sum_list(nums))

bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}

pprint(bst_tree_node)