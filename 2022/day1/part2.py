def solution(lines):
    current_elf = 0
    max_elf = [0]
    
    for line in lines:
        if len(line) == 0 or line.isspace():
            min_elf = min(max_elf) # sum1
            if len(max_elf) < 3:
                max_elf.append(current_elf)
            elif current_elf > min_elf:
                max_elf.remove(min_elf)
                max_elf.append(current_elf)
            
            current_elf = 0
        else:
            current_elf += int(line)
    
    return sum(max_elf)

    
def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()