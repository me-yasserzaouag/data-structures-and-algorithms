# Data Structures and Algorithms
A collection of data structures and algorithm problems implemented in Python.

## Problems
### Subarray Sum (Fixed)
Given an array `nums` containing only non-negative integers, find the largest sum among all contiguous subarrays of length `k`.

For example:
```
nums = [1, 2, 3, 7, 4, 1]
k = 3
```
The length-3 subarrays are:
```
[1, 2, 3] → 6
[2, 3, 7] → 12
[3, 7, 4] → 14
[7, 4, 1] → 12
```
Therefore, the answer is:
```
14
```

#### Approach
This problem can be solved efficiently using a sliding window.

Instead of calculating the sum of every subarray from scratch:

1. Calculate the sum of the first window of size `k`.
2. Move the window one position to the right.
3. Subtract the element that leaves the window.
4. Add the new element that enters the window.
5. Keep track of the maximum window sum.

This reduces the time complexity from `O(n × k)` to `O(n)`.

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

#### Files
```
Subarray Sum (Fixed)/
├── problem.md
└── solution.py
```

#### Implementation Note
The current solution.py contains a small initialization bug:
```python
for num in range(k):
    window_sum += num
```
This adds the indices `0, 1, ..., k - 1` rather than the first `k` values from nums.

It should be:
```
for num in range(k):
    window_sum += nums[num]
```
With that correction, the sliding-window implementation correctly produces `14` for the example above.

## Repository Structure
Each problem is organized in its own directory and contains:
- `problem.md` — problem statement and examples.
- `solution.py` — Python implementation of the solution.
