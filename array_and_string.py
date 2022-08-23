#rite a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
#The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.


def uncompress(s):
  numbers = "0123456789"
  result = []
  i = 0
  j = 0 
  while i < len(s):
    if s[i] in numbers:
      i += 1
    else:
      num = int(s[j:i])
      result.append(s[i] * num )
      i += 1 
      j = i 
      
  return ''.join(result)
#  testing 123 123 123 123


#Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

def compress(s):
  s += "!"
  result = []
  i = 0
  j = 0 

  while j < len(s):
    if s[i] == s[j]:
      j += 1 
    else:
      num = j - i
      if num != 1:
        result.append(str(num))
        result.append(s[i])
      else:
        result.append(s[i])
      i = j 
      
  return "".join(result)


  #Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)
  
def char_count(string):
  new_hash = {}
  for char in string:
    if char not in new_hash:
      new_hash[char] = 0
    new_hash[char] += 1
    
  return new_hash