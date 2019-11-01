from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            dic[tuple(sorted(i))].append(i)
        result = []
        for i in dic:
            result.append(dic[i])
        return result
