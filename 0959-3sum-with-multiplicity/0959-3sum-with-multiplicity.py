class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        i, tuple_count = 0, 0
        instance = {}
        mod = 10 ** 9 + 7

        for ele in arr:
            if ele in instance:
                instance[ele] += 1
            else:
                instance[ele] = 1

        while i < len(arr) - 2:

            j, k = i, len(arr) - 1
            while j < k:
                sum3 = arr[i] + arr[j] + arr[k]

                if sum3 < target:
                    j += instance[arr[j]]

                elif sum3 > target:
                    k -= instance[arr[k]]

                else:
                    if arr[i] != arr[j] != arr[k]:
                        tuple_count += instance[arr[i]] * instance[arr[j]] * instance[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:
                        tuple_count += (instance[arr[i]] * (instance[arr[i]]-1) * instance[arr[k]])//2
                    elif arr[i] != arr[j] == arr[k]:
                        tuple_count += (instance[arr[i]] * instance[arr[j]] * (instance[arr[j]]-1))//2
                    else:
                        tuple_count += (instance[arr[i]] * (instance[arr[i]]-1) * (instance[arr[i]]-2))//6
                    
                    j += instance[arr[j]]
                    k -= instance[arr[k]]

            i += instance[arr[i]]
        return tuple_count % mod
            
        