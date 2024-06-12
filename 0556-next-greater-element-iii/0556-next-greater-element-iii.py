class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # create a list
        arr = list(str(n))
        
        # find suffix and pivot
        suffix = len(arr)-1
        while suffix >=0 and arr[suffix-1] >= arr[suffix]:
            suffix -= 1
        pivot = suffix -1

        if suffix == -1:
            return -1

        #find next pivot
        j = len(arr)-1
        while arr[j] <= arr[pivot]:
            j -= 1
        new_pivot = j

        #swap the pivots
        arr[pivot], arr[new_pivot] = arr[new_pivot], arr[pivot]

        # reverse part from suffix
        j = len(arr)-1
        while j > suffix:
            arr[suffix], arr[j] = arr[j], arr[suffix]
            suffix += 1
            j -= 1

        # res 
        res = int(''.join(arr))
        

        if (res < 2**31) and (res > n):
            return res
        else:
            return -1
        


