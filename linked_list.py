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
    