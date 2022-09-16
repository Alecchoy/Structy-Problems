def linked_list_values(head):
  result = []
  current = head
  while current is not None:
    result.append(current.val)
    current = current.next 
  return result 
