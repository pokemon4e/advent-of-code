def solution(lines):
    sum = 0
    
    for line in lines:
        sum += calc_line(line)
    
    return sum

def calc_line(line):
    length = len(line)
    half = length // 2
    chars = set()
    for i in range(0, half):
        chars.add(line[i])
    
    for i in range(half, length):
        char = line[i]
        if char in chars:
           return get_char_value(char)

def get_char_value(char):
    ascii = ord(char)
    if ascii >= 97:
        return ascii - 96
    else:
        return ascii - 64 + 26

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()