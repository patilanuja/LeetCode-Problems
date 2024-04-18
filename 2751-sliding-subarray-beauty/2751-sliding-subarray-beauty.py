from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums)
        sortedNums = SortedList(nums[:k])

        ans = [sortedNums[x-1] if sortedNums[x-1] < 0 else 0]

        for i in range(k,n):
            # remove the left element from the window
            sortedNums.remove(nums[i - k])
            # add new ele in the window
            sortedNums.add(nums[i])
            # append the beauty ele into the list
            ans.append(sortedNums[x-1] if sortedNums[x-1] < 0 else 0 )
        return ans






        