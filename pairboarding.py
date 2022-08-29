# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# "{)[])}"

# iterate through the string
# check what character it is at the index
# a variable tracking what is the current character that needs to bechecked
# check what the next character is at the 2nd index and if its the different the current char needs to change and
# par = [ '(', ')'] 
# cur = ['{', '}']
# arr = ['[',']']

def closingbrackets(s):
  par = [ '(', ')'] 
  cur = ['{', '}']
  arr = ['[',']']
  i = 0
  j = 0
  while j < len(s):
    if s[j] == par[0]:
      if s[j + 1] == par[1]
     
  