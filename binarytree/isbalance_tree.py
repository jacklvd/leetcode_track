"""
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""


def isBalanced(root):
    # # using top-down approach
    # def height(r):
    #     if not r:
    #         return -1 # empty tree will height of -1
    #     return max(height(r.left), height(r.right)) + 1

    # if not root:
    #     return True
    # return abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(root):
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return dfs(root) != -1
