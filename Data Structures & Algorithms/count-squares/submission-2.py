class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for p in self.points:
        
            if abs(p[0]-point[0]) == abs(p[1]-point[1]) and point[0] != p[0]:

                cor1 = (point[0],p[1])
                cor2 = (p[0],point[1])
                cor3 = (p[0],p[1])
                cor4 = (point[0],point[1])
                if cor4 in self.points:
                    ans += self.points[cor1] * self.points[cor2]*self.points[cor3]*self.points[cor4]
                else:
                    ans += self.points[cor1] * self.points[cor2]*self.points[cor3]
        
        return ans
