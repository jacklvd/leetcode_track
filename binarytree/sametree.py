"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkPreOrderTraversal(root):
            if not root:
                return []
            left = checkPreOrderTraversal(root.left) if root.left else ["none"]
            right = checkPreOrderTraversal(root.right) if root.right else ["none"]
            return [root.val] + left + right

        tree1, tree2 = checkPreOrderTraversal(p), checkPreOrderTraversal(q)
        print(tree1)
        print(tree2)

        return tree1 == tree2
