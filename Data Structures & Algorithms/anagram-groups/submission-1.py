class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        loa = [["".join(sorted(strs[0])),strs[0]]]
        for i in range(1, len(strs)):
            flag = False
            for j in loa:

                if j[0] == ''.join(sorted(strs[i])):
                    j.append(strs[i])
                    flag = True
                    break
                
            if flag == False:
                loa.append([''.join(sorted(strs[i])), strs[i]])
        
        for k in loa:
            del k[0]
        
        return loa
                
                

            