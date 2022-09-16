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

def reverse_list(head):
  current = head
  prev = None
  
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def zipper_lists(head_1, head_2):
  tail = head_1
  current1 = head_1.next
  current2 = head_2 
  count = 0 
  
  while current1 is not None and current2 is not None:
    if count % 2 == 0:
      tail.next = current2
      current2 = current2.next 
    else:
      tail.next = current1 
      current1 = current1.next 
    tail = tail.next
    count += 1
    
  if current1 is not None:
    tail.next = current1
  if current2 is not None:
    tail.next = current2 
  
  return head_1
    

    
