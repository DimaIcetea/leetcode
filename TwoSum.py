# Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так, 
# чтобы они составляли в суммеtarget .
# Вы можете предположить, что каждый вход будет иметь ровно одно решение , 
# и вы не можете использовать один и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
         for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                  print([i, j])

if __name__ == '__main__':
    problem = Solution()
    problem.twoSum([1,3,5,7], 6)
