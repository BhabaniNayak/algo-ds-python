'''
Prompt:
Can you write a function that reverses an inputted string without using the built-in Array#reverse method?

Let's look at some examples. So, calling:
- reverseString("jake") should return "ekaj".
- reverseString("reverseastring") should return "gnirtsaesrever".

Constraints
- Do not use the built-in #reverse() method or [::-1] if Python
- Ideal solution would run in O(n) time complexity and O(1) space complexity
'''

'''
Solution:

Brute force approach - iterate each character in the string and add it to the beginning of a new string.
Time complexity: O(n) - iterate on each character in the string
Space complexity: O(n) - we are creating a new string for each character in the string.

Optimal approach - iterate through the string and swap the first and last characters, then the second and second to last characters, etc.
    - TWO POINTERS technique can be used here
    - Need two pointers to track the first and last characters. Index or the value? Index would be ideal to track
    - Stopping criteria: 
          - length can be even or odd. 
                - If odd, we can stop when the two pointers are equal. 
                - If even, we can stop when the first pointer is greater than the second pointer.
    - Return: reversed string. can not do inplace as strings are not mutable in Python
Time complexity: O(n) - iterate on each character in the string
Space complexity: O(1) - we are not creating any new data structures

Fundamental python concepts review:
  - strings are immutable in Python, so we can not do an in-place swap. transformation algorithms are necessary to create a new string object
  - how to convert a string to a list of characters 
      - list(string)
  - how to convert a list of characters back to a string 
      - ''.join(list)
'''

def reverse_string(input: str) -> str:
    input_list = list(input)
    left, right = 0, len(input) - 1

    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1
    return ''.join(input_list)
    
print(reverse_string("jake")) # should return "ekaj"