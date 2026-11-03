class Solution:
    def isHappy(self, n: int) -> bool:

        numSet= set()
        while True:
            new_number = 0
            while n > 0:
                digit = n%10
                new_number += digit**2
                n = n//10
            
            if new_number == 1:
                return True
            if new_number in numSet:
                break
            numSet.add(new_number)
            n = new_number
        
        return False
        