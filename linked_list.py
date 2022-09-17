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

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy 
  current_1 = head_1 
  current_2 = head_2 
  
  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1 
      current_1 = current_1.next 
    else:
      tail.next = current_2 
      current_2 = current_2.next 
    tail = tail.next 
    
  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2 
    
  return dummy.next

def is_univalue_list(head):
  current = head
  value = current.val 
  while current is not None:
    if current.val != value:
      return False 
    current = current.next 
  
  return True

def longest_streak(head):
  max_streak = 0
  current_streak = 0 
  prev_val = None
  
  current_node = head
  while current_node is not None:
    if current_node.val == prev_val:
      current_streak += 1 
    else:
      current_streak = 1 
    
    prev_val = current_node.val 
    
    if max_streak < current_streak:
      max_streak = current_streak
      
    current_node = current_node.next 
    
  return max_streak 


def remove_node(head, target_val):
  current = head 
  
  prev = None 
  if current.val == target_val:
    return head.next 
  
  while current is not None:
    if current.val == target_val:
      prev.next = current.next 
      break
    prev = current 
    current = current.next 
  return head
      

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  count = 0 
  current = head 
  prev = None
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head 
  
  while current is not None:
    if count == index - 1:
      temp = current.next 
      current.next = Node(value)
      current.next.next = temp
    current = current.next 
    count += 1 
    
  return head 


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head 
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next 

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1 
  current_2 = head_2
  carry = 0
  
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val 
    val_2 = 0 if current_2 is None else current_2.val 
    sum = val_1 + val_2 + carry 
    carry = 1 if sum > 9 else 0 
    digit = sum % 10 
    
    tail.next = Node(digit)
    tail = tail.next 
    
    if current_1 is not None:
      current_1 = current_1.next 
      
    if current_2 is not None:
      current_2 = current_2.next 
  
  return dummy_head.next 



      

    
