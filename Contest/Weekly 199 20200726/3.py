"""
1530. Number of Good Leaf Nodes Pairs
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        path_list = []
        def traverse_nodes(current_node, path_str):
            if current_node is None:
                return
            elif current_node.left is None and current_node.right is None:
                path_list.append(path_str)
                return
            else:
                traverse_nodes(current_node.left, path_str+"l")
                traverse_nodes(current_node.right, path_str+"r")
            
#         def get_distance(str1, str2):
#             if str1 == "":
#                 return len(str2)
#             if str2 == "":
#                 return len(str1)
#             if str1 == str2:
#                 return 0
#             return min(get_distance(str1[:-1], str2)+1, get_distance(str1, str2[:-1])+1)
        
        def get_distance(str1, str2):
            if str1 == "":
                return len(str2)
            if str2 == "":
                return len(str1)
            
            common_digits = 0
            for i in range(min(len(str1), len(str2))):
                if str1[i] == str2[i]:
                    common_digits += 1
                else:
                    break
            
            return (len(str1) + len(str2) - common_digits*2)
        
        
        count = 0
        traverse_nodes(root, "")
        if len(path_list) < 2:
            return 0
            
        for i in range(len(path_list)):
            for j in range(i+1, len(path_list)):
                # print(i, j)
                # print(get_distance(path_list[i], path_list[j]))
                if get_distance(path_list[i], path_list[j]) <= distance:
                    count += 1
        return count