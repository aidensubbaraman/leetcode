class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sLength = len(s)

        finalNum = 0

        for i in range(sLength):

            # M Case
            if s[i] == "M":
                if i != 0 and s[i - 1] == "C":
                    finalNum += 800 # 1000 - 100 - 100 

                else:
                    finalNum += 1000

            # D Case
            elif s[i] == "D":
                if i != 0 and s[i - 1] == "C":
                    finalNum += 300 # 500 - 100 - 100

                else:
                    finalNum += 500

            # C Case
            elif s[i] == "C":
                if i != 0 and s[i - 1] == "X":
                    finalNum += 80 # 100 - 10 - 10

                else:
                    finalNum += 100

            # L Case
            elif s[i] == "L":
                if i != 0 and s[i - 1] == "X":
                    finalNum += 30 # 50 - 10 - 10

                else:
                    finalNum += 50

            # X Case
            elif s[i] == "X":
                if i != 0 and s[i - 1] == "I":
                    finalNum += 8 # 10 - 1 - 1

                else:
                    finalNum += 10

            # V Case
            elif s[i] == "V":
                if i != 0 and s[i - 1] == "I":
                    finalNum += 3 # 5 - 1 - 1

                else:
                    finalNum += 5

            # I Case
            elif s[i] == "I":
                finalNum += 1
        
        return finalNum
        