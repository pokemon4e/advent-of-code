def solution(lines):
    sum = 0
    for line in lines:
        digits = [int(x) for x in line if x.isdigit()]
        sum += digits[0] * 10 + digits[-1]

    return sum

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()