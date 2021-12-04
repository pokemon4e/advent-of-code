def solution(directios):
    horizontal = 0
    depth = 0
    aim = 0
    for d in directios:
        direction = d[0]
        units = int(d[1])
        
        match direction:
            case 'forward':
                horizontal += units
                depth += aim * units
            case 'up':
                aim -= units
            case 'down':
                aim += units
                
    return horizontal * depth
    
def read_input(filename):
    with open(filename) as f:
        return [l.split() for l in f.readlines()]
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()