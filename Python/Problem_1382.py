
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Create list to hold value of bst
        inorder = []

        #DFS to get nodes in orderes
        def dfs(node: TreeNode):
            
            #If the node you are on doesn't exist return none
            if node == None:
                return
            
            #Recursively call other function and pass in left node
            dfs(node.left)
            #Append current node value to list
            inorder.append(node.val)
            #Move to right node
            dfs(node.right)
        
        

        def build_bst(inorder: list[int]) -> TreeNode:
            #Check if list is empty
            if not inorder:
                return
            #Get the middle of the list
            mid = len(inorder)//2

            #Create a TreeNode instance
            newRoot = TreeNode(inorder[mid])
            #Recursively call function to build out left side using left half list
            newRoot.left = build_bst(inorder[:mid])
            #Recursively call function to build out right side using right half list
            newRoot.right = build_bst(inorder[mid+1:])

            #Return the node
            return newRoot
        
        dfs(root) 
        return build_bst(inorder)
