class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0: return ""
        
        longPrefix = strs[0]
        
        for string in strs:
            for i in range(0, len(longPrefix)):
                if (i >= len(string) or longPrefix[i] != string[i]):
                    longPrefix = longPrefix[0:i]
                    break
                
        return longPrefix
