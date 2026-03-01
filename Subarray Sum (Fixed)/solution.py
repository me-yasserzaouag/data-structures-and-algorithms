def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = 0
    for num in range(k):
        window_sum += num
    ans = window_sum
    
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        ans = max(ans, window_sum)
    return ans