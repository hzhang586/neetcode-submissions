class Solution:
    single = set()
    double = set()
    for i in range(1,10):
        single.add(str(i))

    for i in range(10,27):
        double.add(str(i))
    print(single)
    print(double)
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        if len(s) == 1:
            return 1 if s[0] in self.single else 0
        prev_2 = 1 if s[0] in self.single else 0
        prev_1  = 0 
        if s[0] in self.single and s[1] in self.single and s[:2] in self.double:
            prev_1 = 2
        elif s[0] in self.single and s[1] in self.single:
            prev_1 = 1
        elif s[:2] in self.double:
            prev_1 = 1
        else:
            prev_1  = 0
        

    
        for i in range(2,n):
            cur = 0
            if s[i] in self.single:
                cur += prev_1
            if s[i-1:i+1] in self.double:
                cur += prev_2
                
            
            prev_2 = prev_1
            prev_1 = cur
        
        return prev_1
        