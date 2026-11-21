class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = []
        if nums == []:
            return 0
        for i in nums:
            if sol == []:
                sol.append([i])
            else:
                add1 = False
                for j in sol:
                    if j[0] - 1 == i and add1 == False:
                        j.insert(0,i)
                        add1 = j
                    elif j[-1] + 1 == i and add1 == False:
                        j.append(i)
                        add1 = j
                    elif add1 and j[0] - 1 == i:
                        temp = add1
                        add1 = add1 + j
                        sol.remove(temp)
                        sol.remove(j)
                        sol.append(add1)
                        add1 = True
                    elif add1 and j[-1] + 1 == i:
                        temp = j
                        j = j + add1
                        sol.remove(temp)
                        sol.remove(add1)
                        sol.append(j)
                        add1 = True

                if add1 == False and [i] not in sol:
                    sol.append([i])
        max_length = max(len(set(sublist)) for sublist in sol)
        return max_length
                        
                        
            
        