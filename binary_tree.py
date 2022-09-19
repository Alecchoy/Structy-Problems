def depth_first_values(root):
  if not root:
    return []
  
  values = []
  stack = [root]

  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values

def breadth_first_values(root):
  if not root:
    return []
  
  answer = []
  
  queue = [root]
  while queue:
    node = queue.pop(0)
    answer.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  
  
  return answer


def depth_first_values(root):
  if root is None:
    return []
  left = depth_first_values(root.left)
  right = depth_first_values(root.right)
  
  return [root.val] + left + right

def breadth_first_values(root):
  if not root:
    return []
  
  answer = []
  
  queue = [root]
  while queue:
    node = queue.pop(0)
    answer.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  
  
  return answer
    
  
    