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

from tkinter.tix import FileEntry


def closingbrackets(s):
  par = [ '(', ')'] 
  cur = ['{', '}']
  arr = ['[',']']
  i = 0
  j = 0
  while j < len(s):
    if s[j] == par[0]:
      if s[j + 1] == par[1]


def closingbrackets(s):
  stack = []
  parens = {
    '}' : '{',
    ']' : '[',
    ')' : '('
  }
  
  for c in s:
    if c not in parens:
      stack.append(c)
    else:
      if stack and stack[-1] == parens[c]:
        stack.pop()
      else:
        return False 
  if not stack:
    return True
     
  def compress(s):
  i = 0
  j = 0
  result = ''
  
  while j < len(s) - 1:
    if s[j] == s[i]:
      j += 1
    else:
      number = j - i
      if number == 1:
        result += (s[i])
      else:
        result += (str(number))
        result += (s[i])
    i = j
  return result
  


  #Car Fleet 

  var carFleet = function(target, position, speed){

  };

  #pairboarding



  leaf list
Write a function, leafList, that takes in the root of a binary tree and returns an array containing the values of all leaf nodes in left-to-right order.

test_00:
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

leafList(a); // -> [ 'd', 'e', 'f' ] 
test_01:
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");
const g = new Node("g");
const h = new Node("h");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h

leafList(a); // -> [ 'd', 'g', 'h' ]
test_02:
const a = new Node(5);
const b = new Node(11);
const c = new Node(54);
const d = new Node(20);
const e = new Node(15);
const f = new Node(1);
const g = new Node(3);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
e.left = f;
e.right = g;

//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3

leafList(a); // -> [ 20, 1, 3, 54 ]
test_03:
const x = new Node('x');

//      x

leafList(x); // -> [ 'x' ]
test_04:
leafList(null); // -> [ ]

# i wan



##








node.val
node.left
node.right


// want to return array of all leaf nodes
// leaf node - node w/ no children <-- must have some conditional to check if leaf node and push to result array

const leafList = (root) => {
	const leaves = [];
  _leafList(root, leaves);
  return leaves;
};

const _leafList = (root, leaves) => {
	if (root === null) return;
  
  if (root.left === null && root.right === null) leaves.push(node.val);
  
  _leafList(root.left, leaves);
  _leafList(root.right, leaves);
};

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

// unshift(~) <-- O(n)

// push() O(1)
// reverse() O(1)
