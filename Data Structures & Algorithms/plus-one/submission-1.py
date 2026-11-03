class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        flag = 0
        digits[-1] += 1

        for i in range(len(digits)-1,-1,-1):
            
            digit = (digits[i]+flag) % 10
            if digits[i]+flag >= 10:
                flag =1
            else:
                flag = 0
            digits[i] = digit
            if not flag:
                break
        
        if flag:
            digits.insert(0,1)
        
        return digits
        


        