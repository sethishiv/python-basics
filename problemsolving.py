'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(len(nums)):
            p = target-nums[i]
            if p in nums:
                a=nums.index(p)
                if a==i:
                    continue
                break
        return i,a'''


def is_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False


year = int(input( "enter year: "))
print(is_leap(year))