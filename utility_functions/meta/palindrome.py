"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

----------------------------------------------------------------------------------

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(" "))  # Output: True
print(isPalindrome("0P"))  # Output: False
```

### Explanation:
1. **Initialization**:
   - `left` starts from the beginning of the string.
   - `right` starts from the end of the string.

2. **Two-pointer Approach**:
   - Move `left` forward until an alphanumeric character is found.
   - Move `right` backward until an alphanumeric character is found.
   - Compare the characters at `left` and `right` after converting them to lowercase.
   - If they are not equal, return `False`.
   - If they are equal, move both pointers towards each other (`left` increases, `right` decreases).

3. **Loop Termination**:
   - The loop terminates when `left` is no longer less than `right`, meaning all characters have been checked.
   - If no mismatches were found, the string is a palindrome, and the function returns `True`.

### Complexity:
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string. Each character is processed at most once.
- **Space Complexity**: \(O(1)\), no extra space proportional to the input size is used.

This solution efficiently checks if the given string is a palindrome by ignoring non-alphanumeric characters and treating uppercase and lowercase letters as equal.

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
    
"""
----------------------------------------------------------------------------------------------------
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1

        def is_palindrome(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left+1,right) or is_palindrome(left, right-1)
            left += 1
            right -= 1
        return True