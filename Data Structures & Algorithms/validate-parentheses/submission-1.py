class Solution:
    def isValid(self, s: str) -> bool:

        stac = []
        for i,x in enumerate(s):
            if stac:
                if x == ')':
                    if stac[-1] == '(':
                        stac.pop()
                        continue
                elif x ==']':
                    if stac[-1] == '[':
                        stac.pop()
                        continue
                elif x == '}':
                    if stac[-1] == '{':
                        stac.pop()
                        continue
                
            stac.append(x)
        
        print(stac)
        
        return True if not stac else False
        