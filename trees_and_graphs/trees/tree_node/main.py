from tree import TreeNode

# ________Main Program_________ # 
root = TreeNode("Root Node")
first_child = TreeNode("First Child Node")
second_child = TreeNode("Second Child Node")
third_child = TreeNode("Third Child Node")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()
