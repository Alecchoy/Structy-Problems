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

def tree_sum(root):
  if not root:
    return 0 
  sum = 0 
  queue = [root]
  while queue:
    node = queue.pop(0)
    sum += node.val
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  
  return sum


def tree_includes(root, target):
  if not root:
    return False 
  queue = [root]
  
  while queue:
    node = queue.pop(0)
    if node.val == target:
      return True 
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return False 
    
def tree_min_value(root):
  queue = [root]
  test = float("inf")
  while queue:
    node = queue.pop(0)
    if test > node.val:
      test = node.val 
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return test 


def max_path_sum(root):
  if root is None:
    return float('-inf')
  
  if root.left is None and root.right is None:
    return root.val
  
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))

def path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [root.val] + left_path 
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [root.val] + right_path 
    
  return None
  
    
    