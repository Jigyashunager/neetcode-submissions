class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            dict1[s[index]] = 1 + dict1.get(s[index], 0)
            dict2[t[index]] = 1 + dict2.get(t[index], 0)
        return dict1 == dict2
