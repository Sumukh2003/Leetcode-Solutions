class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for char_s,char_t in zip(s,t):
            if char_s in st:
                if st[char_s]!=char_t:
                    return False
            else:
                st[char_s]=char_t
            if char_t in ts:
                if ts[char_t]!=char_s:
                    return False
            else:
                ts[char_t]=char_s
        return True

