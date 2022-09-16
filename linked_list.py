def linked_list_values(head):
  result = []
  current = head
  while current is not None:
    result.append(current.val)
    current = current.next 
  return result 


def sum_list(head):
  sum = 0
  current = head
  while current is not None:
    sum += current.val 
    current = current.next
  
  return sum


def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True 
    current = current.next 
  return False 


def get_node_value(head, index):
  idx = 0 
  current = head
  while current is not None:
    if idx == index:
      return current.val
    current = current.next
    idx += 1
  return None
    
