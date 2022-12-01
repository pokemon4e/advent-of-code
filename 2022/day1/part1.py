def solution(lines):
    current_elf = 0
    max_elf = 0
    
    for line in lines:
        if len(line) == 0 or line.isspace():
            max_elf = max(current_elf, max_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    
    return max_elf

    
def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()