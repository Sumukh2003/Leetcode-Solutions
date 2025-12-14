import re
class Solution(object):
    
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        allowed_types=["electronics", "grocery", "pharmacy", "restaurant"]
        order={name:idx for idx , name in enumerate(allowed_types)}
        valid=[]
        for c,b,a in zip(code,businessLine,isActive):
            if not a:
                continue
            if b not in order:
                continue
            if not c or not re.match(r'^[A-Za-z0-9_]+$',c):
                continue
            valid.append((order[b],c))
        valid.sort(key=lambda x:(x[0],x[1]))
        return [c for _,c in valid]
