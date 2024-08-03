"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.

Approach:
Use two pointers, one for the string (i) and one for the abbreviation (j).
Iterate through the abbreviation:
If the current character in the abbreviation is a digit, read the full number and move the pointer in the string by that number.
If the current character in the abbreviation is a letter, it must match the current character in the string.
Ensure that both pointers reach the end of their respective strings.
Example:
Input: word = "internationalization", abbr = "i18n"
Output: True


To determine if a given string matches a given abbreviation, we need to parse both the string and the abbreviation simultaneously and check if the characters and the numerical values in the abbreviation correspond correctly to the characters in the string.

### Approach:
1. Use two pointers, one for the string (`i`) and one for the abbreviation (`j`).
2. Iterate through the abbreviation:
   - If the current character in the abbreviation is a digit, read the full number and move the pointer in the string by that number.
   - If the current character in the abbreviation is a letter, it must match the current character in the string.
3. Ensure that both pointers reach the end of their respective strings.


# Test cases
print(validWordAbbreviation("internationalization", "i18n"))  # Output: True
print(validWordAbbreviation("apple", "a2e"))  # Output: True
print(validWordAbbreviation("apple", "a3e"))  # Output: False
print(validWordAbbreviation("apple", "4e"))  # Output: False (because '4' should match "appl")
print(validWordAbbreviation("substitution", "s10n"))  # Output: True
print(validWordAbbreviation("substitution", "sub4u4"))  # Output: False
```

### Explanation:
1. **Initialization**: Start with two pointers, `i` for `word` and `j` for `abbr`.
2. **Digit Handling**:
   - If `abbr[j]` is a digit, compute the full number (handle multi-digit numbers).
   - Move the `i` pointer in `word` by the computed number.
   - Ensure no leading zeros in the abbreviation numbers.
3. **Character Matching**:
   - If `abbr[j]` is a letter, it must match the current character in `word`.
   - Increment both pointers if they match.
4. **Termination Check**:
   - Both pointers should reach the end of their respective strings simultaneously for a valid match.

### Complexity:
- **Time Complexity**: \(O(n + m)\), where \(n\) is the length of the word and \(m\) is the length of the abbreviation. Each character in both strings is processed once.
- **Space Complexity**: \(O(1)\), since no additional space proportional to the input size is used.
"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        # two pointer to track
        i,j = 0,0

        while i < len(word) and j < len(abbr):
            #  check if jth location is a digit
            if abbr[j].isdigit():
                if abbr[j]=='0':
                    return False # leading zero not allowed
            
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num*10 + int(abbr[j])
                    j += 1
                i += num
            else: # characters
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i==len(word) and j==len(abbr)