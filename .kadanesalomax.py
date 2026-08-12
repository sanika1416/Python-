from typing import List

def max_subarray(nums: List[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]

    for num in range(1, len(nums)):

        if nums[i] > current_sum + nums[i]:
            current_sun = nums[i]
        else:
            current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum 

        return max_sum       

