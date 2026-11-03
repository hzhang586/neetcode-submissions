class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point
        for x2,y2 in self.points:
        
            if abs(x-x2) == abs(y-y2) and x != x2:
                ans += self.points[(x,y2)]*self.points[(x2,y)]*self.points[(x2,y2)]
        
        return ans
