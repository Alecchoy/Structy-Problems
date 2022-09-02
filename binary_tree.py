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


  