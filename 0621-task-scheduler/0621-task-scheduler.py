class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## TC: O(n)
        ## SC: O(1)

        # Calculate freq of each CPU tasks
        freq = collections.Counter(tasks)

        # find max_freq 
        max_freq = max(freq.values())

        # list all the values (to calculate max_freq_ele_count)
        freq = list(freq.values())

        max_freq_ele_count = 0
        i = 0

        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_ele_count += 1
            i += 1
            
        ans = (max_freq - 1) * (n + 1) + max_freq_ele_count

        return max(ans, len(tasks))
