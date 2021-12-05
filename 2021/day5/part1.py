from collections import defaultdict

class point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y

    def __hash__(self) -> int:
        return hash((self.__x, self.__y))
    
    def __eq__(self, __o: object) -> bool:
        return (isinstance(__o, type(self)) and 
               (self.__x, self.__y) == (__o.x, __o.y))

def solution(lines):
    points_totals = defaultdict(int)

    for l in lines:
        p = l.split(' -> ')
        p1 = [int(c) for c in p[0].split(',')]
        p2 = [int(c) for c in p[1].split(',')]
                
        minX = min(p1[0], p2[0])
        maxX = max(p1[0], p2[0])
        minY = min(p1[1], p2[1])
        maxY = max(p1[1], p2[1])
        if minX == maxX: #vertical
            for y in range(minY, maxY  + 1):
                points_totals[point(minX, y)] += 1
        elif minY == maxY: #horizontal
            for x in range(minX, maxX + 1):
                points_totals[point(x, minY)] += 1
        
    return len([p for p, total in points_totals.items() if total > 1])    
    
def read_input(filename):
    with open(filename) as f:
        return f.readlines()
            
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()