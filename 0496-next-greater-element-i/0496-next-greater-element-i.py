class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums1)
        map = {}
        stack = [] # 1
        res = [-1]*l
        
        for i in range(len(nums1)):
            map[nums1[i]] = i

        print(map)


        for n in nums2:
            while stack and stack[-1] < n:
                res[map[stack[-1]]] = n
                stack.pop()

            if n in nums1:
                stack.append(n)

        return res           


