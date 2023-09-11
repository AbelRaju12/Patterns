class TreeNode:
    def __init__(self, key):
        self.leftnode = None
        self.rightnode = None
        self.val = key
        
def build_tree():
    root_val = int(input("Enter the root element: "))
    root = TreeNode(root_val)
    q = []
    q.append(root) # q = [root]
    
    while q:
        current_node = q.pop(0)
        
        left_child = input(f"Enter the left child for {current_node.val}: ")
        if left_child != 'none':
            current_node.leftnode = TreeNode(int(left_child))
            q.append(current_node.leftnode)
            
        right_child = input(f"Enter the right child for {current_node.val}: ")
        if right_child != 'none':
            current_node.rightnode = TreeNode(int(right_child))
            q.append(current_node.rightnode)
            
    return root


def inorder_traversal(node):
    if node:
        inorder_traversal(node.leftnode)
        print(node.val, end=' ')
        inorder_traversal(node.rightnode)
    
if __name__ == "__main__":
    root = build_tree()
    
    print("The inorder traversal of the tree :")
    inorder_traversal(root)        