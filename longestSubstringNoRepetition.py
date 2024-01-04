class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sLength = len(s)
        longestSubString = 0
        currentCount = 0
        currentSubstring = set()

        i = 0
        j = 0

        while i < sLength and j < sLength:

            if s[j] not in currentSubstring:
                currentSubstring.add(s[j])
                j += 1
                currentCount = j - i
                longestSubString = max(longestSubString, currentCount)
            else:
                currentSubstring.remove(s[i])
                i += 1

        return longestSubString
        