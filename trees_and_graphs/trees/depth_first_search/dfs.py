from tree_node import TreeNode, print_tree, print_path

def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    node_found = dfs(child, target, path)

    if node_found is not None:
      return node_found

  return None

# ________Main Program_________ # 
sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]

print_tree(sample_root_node)
