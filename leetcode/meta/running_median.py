'''
Median Stream
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).

The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

Signature
int[] findMedian(int[] arr)

Input
n is in the range [1, 1,000,000].
Each value arr[i] is in the range [1, 1,000,000].

Output
Return a list of n integers output[0..(n-1)], as described above.

Example 1
n = 4
arr = [5, 15, 1, 3]
output = [5, 10, 5, 4]
The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.

Example 2
n = 2
arr = [1, 2]
output = [1, 1]
The median of [1] is 1, the median of [1, 2] is (1 + 2) / 2 = 1.5 (which should be rounded down to 1).
'''

# def calculate_median(input):
#     sorted_input = sorted(input) # O(nlogn)
#     input_len = len(input)

#     if input_len % 2 == 1: #odd
#         return sorted_input[input_len//2]
#     else: # even
#         return (sorted_input[input_len//2] + sorted_input[input_len//2 - 1])//2

 
# n = 4
# arr = [5, 15, 1, 3]
# output = [arr[0]]

# for idx in range(1,n): # O(n)
#     output.append(calculate_median(arr[:idx+1]))

# print(output)
# assert output == [5, 10, 5, 4]


# n2 = 2
# arr2 = [1, 2]
# output2 = [arr2[0]]

# for idx in range(1,n2):
#     output2.append(calculate_median(arr2[:idx+1]))

# print(output2)
# assert output2 == [1, 1]


'''

Let's break down the code:

calculate_median function:

sorted_input = sorted(input) : 
This operation sorts the list and has a time complexity of O(nlogn).

input_len = len(input) : 
Getting the length of a list is O(1) time complexity.
The rest of the operations inside the function (checking for even/odd and returning the median) are constant time, O(1).

The for loop:
It runs n times.
Inside the for loop, the line arr[:idx+1] creates a sublist of size idx + 1, which has O(n) time complexity.
calculate_median is then called on this sublist. In the worst case, this sublist will be of size n, making the time complexity of calculate_median to be O(nlogn).
Thus, the for loop has a time complexity of:
O(n) * (O(n) + O(nlogn)) = O(n^2) + O(n^2 * logn)

When combining these complexities, O(n^2 * logn) dominates over O(n^2), so the overall time complexity is:
O(n^2 * logn).

Space Complexity:

The space complexity of the sorted function in the worst case is O(n) because it may require additional space to perform the sort.
The output list has a space complexity of O(n) since it can have up to n elements.
No other data structures in the code have a size dependent on n.
Thus, the overall space complexity is O(n).

'''

##################################################################################################################
# Optimization
##################################################################################################################

'''
The code can be optimized. A key insight is that if you maintain two heaps (a max-heap for the lower half of the data and a min-heap for the upper half), you can calculate the median in constant time.

Here's the optimized approach:

Use a max-heap for the lower half of numbers and a min-heap for the upper half.
After each insertion into the heaps, balance the heaps so that their sizes differ by at most 1.
The median is then either the top of the max-heap, the top of the min-heap, or the average of the two, depending on the total number of elements.
'''

from heapq import heappush, heappop

def add_to_heap(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heappush(lowers, -num)
    else:
        heappush(highers, num)

def balance_heaps(lowers, highers):
    while len(lowers) > len(highers) + 1:
        heappush(highers, -heappop(lowers))
    while len(highers) > len(lowers):
        heappush(lowers, -heappop(highers))

def get_median(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0]) // 2
    else:
        return -lowers[0] if len(lowers) > len(highers) else highers[0]

def calculate_medians(arr):
    lowers, highers = [], []  # max-heap, min-heap
    medians = []

    for num in arr:
        add_to_heap(num, lowers, highers)
        balance_heaps(lowers, highers)
        medians.append(get_median(lowers, highers))

    return medians

n = 4
arr = [5, 15, 1, 3]
output = calculate_medians(arr)
print(output)
assert output == [5, 10, 5, 4]

# Time complexity:
# The loop runs n times, and inside each iteration of the loop, we perform operations with the heaps. 
# Each heap operation (push/pop) is O(log n). Therefore, the overall time complexity is O(n log n).

# Space complexity:
# The space complexity is O(n), coming from the storage of the numbers in the two heaps.

'''
Explanation:

Certainly! Let's break down each function used in the optimized solution:

### 1. `add_to_heap(num, lowers, highers)`

This function decides in which heap (lower or upper half) to place the incoming number. 

- **Parameters**:
  - `num`: The number to be added.
  - `lowers`: The max-heap containing the lower half of the numbers seen so far.
  - `highers`: The min-heap containing the upper half of the numbers seen so far.

- **Functionality**:
  - If `lowers` is empty or if `num` is less than the maximum element of `lowers` (top of max-heap), the number is pushed into `lowers`. We negate `num` because Python's `heapq` provides a min-heap by default; by negating the number, we're effectively using it as a max-heap.
  - Otherwise, the number is pushed into `highers`.

### 2. `balance_heaps(lowers, highers)`

The purpose of this function is to balance the two heaps to ensure that their sizes do not differ by more than 1. This allows us to easily and efficiently find the median.

- **Parameters**:
  - `lowers`: The max-heap for the lower half.
  - `highers`: The min-heap for the upper half.

- **Functionality**:
  - If `lowers` has more than one element than `highers`, elements are popped from `lowers` and pushed to `highers` until they are balanced.
  - Conversely, if `highers` has more elements than `lowers`, elements are popped from `highers` and pushed to `lowers`.

### 3. `get_median(lowers, highers)`

This function retrieves the median based on the top elements of the heaps.

- **Parameters**:
  - `lowers`: The max-heap for the lower half.
  - `highers`: The min-heap for the upper half.

- **Functionality**:
  - If both heaps are of equal size, the median is the average of the top elements of both heaps. (Note: since we are using integer division (`//`), this provides the median for the purpose of this problem.)
  - If one heap is larger, the top element of the larger heap is the median.

### 4. `calculate_medians(arr)`

This is the main function that uses the above helper functions to compute the median after each number in the array.

- **Parameter**:
  - `arr`: The input array of numbers.

- **Functionality**:
  - Initializes two empty lists `lowers` and `highers` for the two heaps.
  - For each number in `arr`:
    - Adds the number to one of the heaps using `add_to_heap`.
    - Balances the heaps using `balance_heaps`.
    - Gets the current median using `get_median` and appends it to the `medians` list.
  - Returns the list of medians.

By maintaining and manipulating the two heaps in this manner, we can efficiently determine the median of the dataset at any given point.
'''

##################################################################################################################
# Applications
##################################################################################################################

'''
The two heaps approach, often referred to as the "median maintenance" technique, can be extended to solve various problems that involve streaming data or real-time processing. Here are some scenarios and problems where this technique can be applied:

1. **Real-time Analytics**:
   - If a company wants to track the median revenue per transaction in real-time as transactions come in, the two heaps approach can be used.
  
2. **Dynamic Order Statistics**:
   - Beyond just the median, the two heaps approach can be adapted to find the k-th largest or k-th smallest element in a dynamically changing dataset. By maintaining heaps of appropriate sizes, we can access any order statistic in constant time.

3. **Sliding Window Median**:
   - Given an array of numbers and a sliding window size `k`, one can use the two heaps approach to efficiently calculate the median of the last `k` numbers as the window slides over the array.

4. **Online Games**:
   - In multiplayer online games where players are continuously scored, you might want to find the player with the median score in real-time or maintain players' ranks dynamically. The two heaps approach can be used here.

5. **Load Balancing**:
   - In systems where tasks arrive dynamically and are assigned a priority, the median priority task can be selected using the two heaps technique to ensure that neither high nor low priority tasks are starved for too long.

6. **E-commerce Recommendations**:
   - For dynamically recommending products based on price, the median-priced product (or products around the median price range) can be shown to the user as they browse.

7. **Temperature Monitoring**:
   - In environmental monitoring systems, where temperatures are being read continuously, the two heaps approach can help in determining the median temperature in real-time, which might be useful to trigger certain actions.

8. **Financial Algorithms**:
   - In trading algorithms, where stock prices are continuously updated, a running median of stock prices can be used as one of the indicators for buy/sell decisions.

9. **Ad Auction Systems**:
   - In real-time ad auction systems, where ads have varying bid values, finding the median bid can be crucial for certain decision-making processes.

The fundamental idea behind the two heaps approach is to maintain a dynamic dataset such that we can efficiently access its middle elements. This concept can be applied in numerous scenarios where real-time or dynamic access to such middle elements (like the median) is required.
'''