# The Two Pointer Technique

The two pointer technique is a near necessity in any software developer's toolkit, especially when it comes to technical interviews. In this guide, we'll cover the basics so that you know when and how to use this technique.

## What is the pattern?
The name two pointers does justice in this case, as it is exactly as it sounds. It's the use of two different pointers (usually to keep track of array or string indices) to solve a problem involving said indices with the benefit of saving time and space.

But what are pointers? In computer science, a pointer is a reference to an object. In many programming languages, that object stores a memory address of another value located in computer memory, or in some cases, that of memory-mapped computer hardware.

## When do we use it?
In many problems involving collections such as arrays or lists, we have to analyze each element of the collection compared to its other elements.

There are many approaches to solving problems like these. For example we usually start from the first index and iterate through the data structure one or more times depending on how we implement our code.

Sometimes we may even have to create an additional data structure depending on the problem's requirements. This approach might give us the correct result, but it likely won't give us the most space and time efficient result.

This is why the two-pointer technique is efficient. We are able to process two elements per loop instead of just one. Common patterns in the two-pointer approach entail:

- Two pointers, each **starting from the beginning and the end** until they both meet.
- One pointer moving at a **slow pace**, while the other pointer moves at **twice the speed**.

These patterns can be used for string or array questions. They can also be streamlined and made more efficient by iterating through two parts of an object simultaneously. 

## Example Problems
- Reverse String
- Two Sum 
- Sorted Two Sum 
- Sliding WIndow Problems
- Detecting cycles in a linked list data structure

# Method Breakdown
- Initialization
    - pointer_one = 0
    - pointer_two = len(arr) - 1
- Increment
    - pointer_one += 1
    - pointer_two -= 1
- Stopping Condition (base condition)
    - while pointer_one < pointer_two
