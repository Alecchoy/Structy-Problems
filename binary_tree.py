#Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

def linked_list_values(head):
  result = []
  current = head
  while current is not None:
    result.append(current.val)
    current = current.next
  return result


#Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

def sum_list(head):
  sum = 0 
  current = head
  while current is not None:
    sum += current.val
    current = current.next 
  
  return sum

  #Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

def linked_list_find(head, target):
  current = head
  
  while current is not None:
    if current.val == target:
      return True
    current = current.next 
      
  return False

#Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

def get_node_value(head, index):
  if head is None:
    return None
  
  if index == 0 
  return head.val 

  return get_node_value(head.next, index - 1)

  #Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

  def reverse_list(head):
  prev = None
  current = head 
  while current is not None:
    next = current.next 
    current.next = prev 
    prev = current 
    current = next 
  
  return prev 


#rite a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.
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




merge lists
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.



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

    