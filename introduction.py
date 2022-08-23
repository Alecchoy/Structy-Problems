# Welcome to Structy! Watch the approach video in the tab at the top of this window to get started.
# Write a function greet that takes in a string argument, s, and returns the string "hey s". No tricks here. Run the tests to check your work.

def greet(s):
  return "hey " + s


print('hello')
print(greet("chicken"))



#Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

#lve this without using any built-in list methods.

#You can assume that the list is non-empty.

def max_value(nums):
  max = float('-inf')
  
  for i in nums:
    if i > max:
      max = i 
      
  return max

#Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

#A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

#For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.


def is_prime(n):
  if n < 2: 
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
    
  return True
    


  