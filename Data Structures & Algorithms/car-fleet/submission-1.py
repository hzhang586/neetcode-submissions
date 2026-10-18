class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ans = 0
        pos_idx_tup_l = [(target-x,i) for i,x in enumerate(position)]
        pos_idx_tup_l.sort(reverse = True)
        def calculate_time(car):
            dist = car[0]
            spe = speed[car[1]]
            return dist/spe
        
        while pos_idx_tup_l:
            last = pos_idx_tup_l.pop()
            time = calculate_time(last)
            ans += 1
            while pos_idx_tup_l:
                if calculate_time(pos_idx_tup_l[-1]) <= time:
                    pos_idx_tup_l.pop()
                else:
                    break
            
        
        return ans







        