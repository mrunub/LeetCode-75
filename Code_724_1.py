# 724. Find Pivot Index
from typing import List
from time import time


def runningSum(nums, start_pos):
    running_sum_list = [0] * len(nums)
    if start_pos == "left":
        for i in range(len(nums)):
            running_sum_list[i] = sum(nums[0:i + 1])
        return running_sum_list
    elif start_pos == "right":
        nums = nums[::-1]
        for i in range(len(nums)):
            running_sum_list[i] = sum(nums[0:i + 1])
        return running_sum_list[::-1]


def pivotIndex(nums: List[int]) -> int:
    sum_from_left = runningSum(nums, "left")
    sum_from_right = runningSum(nums, "right")
    new_list = list(zip(sum_from_left, sum_from_right))
    if sum(nums[1:]) == 0:
        return 0
    for index in range(1, len(nums) - 1):
        if sum_from_left[index] == sum_from_right[index]:
            return index
    if sum(nums[:-1]) == 0:
        if nums[-1] == 0:
            last_index = -1
            while sum(nums[:last_index]) == 0 and nums[last_index] == 0:
                last_index -= 1
            return len(nums) + last_index + 1
        else:
            return len(nums) - 1
    return -1


list_input = [1, 7, 3, 6, 5, 6]

start_time = time()
print(pivotIndex(list_input))
end_time = time()
print(f"Round time : {end_time - start_time}")
