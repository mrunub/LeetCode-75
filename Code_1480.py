# 1480. Running Sum of 1d Array
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    running_sum_list = [0] * len(nums)
    for i in range(len(nums)):
        running_sum_list[i] = sum(nums[0:i + 1])
    return running_sum_list


print(runningSum([1, -1, 3, -3]))
