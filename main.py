from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    answer = []

    for i, num in enumerate(nums):
        complement = target - num

        if complement in answer:
            return [answer.index(complement), i]

        answer.append(num)

    return []
