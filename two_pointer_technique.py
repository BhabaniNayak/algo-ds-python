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
    
# print(reverse_string("jake")) # should return "ekaj"

############################################################################################################

'''
Given an integer array that represents the heights of N buildings. 
The task is to delete N - 2 buildings such that the water that can be trapped between 
the remaining two buildings is maximum. The total water trapped between two buildings 
is a gap between them (the number of buildings removed) multiplied by the height of 
the smaller building.

Input: arr[] = [1, 3, 4]
Output: 1 
Explanation: We have to calculate the maximum water that can be stored between any 2 buildings. 
Water between the buildings of height 1 and height 3 = 0. 
Water between the buildings of height 1 and height 4 = 1. 
Water between the buildings of height 3 and height 4 = 0. 
Hence maximum of all the cases is 1.

Input: arr[] = [2, 1, 3, 4, 6, 5]
Output: 8 
We remove the middle 4 buildings and get the total water stored as 2 * 4 = 8  

'''

'''
Solution:

Brute force approach - iterate through each building and calculate the water trapped between it and every other building.
Time complexity: O(n^2)
Space complexity: O(1)

Optimal approach - use the TWO POINTER technique to iterate through the array and calculate the water trapped between the two buildings.
Time complexity: O(n)
Space complexity: O(1)

'''

def max_water_building(height: list) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # get the height of the small building
        min_height = min(height[left], height[right])
        max_water = max(max_water, min_height*(right - left -1))
        
        # conditional increment of pointers
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water

print(max_water_building([2, 1, 3, 4, 6, 5])) # should return 8
print(max_water_building([1, 3, 4])) # should return 1

############################################################################################################