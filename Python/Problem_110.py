#Given a binary tree, determine if it is height balanced

#Solution: Depth First Search
def dfs(node):

    #Check if you are at the lowest leaf
    if node == None:
        return 0

    #Get left nodes height    
    left = dfs(node.left)
    #Check if left node is not balanced, if unblanced return -1
    if left == -1:
        return -1

    #Get right node height
    right = dfs(node.right)
    #Check if right node is not balanced, if unblanced return -1
    if right == -1:
        return -1
    
    #Check if the difference in height is more than one, if it is node is unbalanced return -1
    if abs(left - right) > 1:
        return -1

    #increment the height of the node based on which node (left or right) is longer
    return 1 + max(left, right)