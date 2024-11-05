class Solution(object):
    def isAnagram(self, s, t):
        conjuntoS, conjuntoT = {}, {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            conjuntoS[s[i]] = 1 + conjuntoS.get(s[i], 0)
        for i in range(len(t)):
            conjuntoT[t[i]] = 1 + conjuntoT.get(t[i], 0)
        for c in conjuntoS:
            if conjuntoS[c] != conjuntoT.get(c, 0):
                return False
        return True
        