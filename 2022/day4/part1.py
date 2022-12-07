def solution(lines):
    sum = 0
    
    for line in lines:
        sum += calc_line(line)
    
    return sum

def calc_line(line):
    input = line.split(',')
    elf1 = get_elf_section(input[0])    
    elf2 = get_elf_section(input[1])    
    
    if is_contained(elf1, elf2) or is_contained(elf2, elf1):
        return 1
    else:
        return 0
    
def get_elf_section(elf):
    input = elf.split('-')
    
    return (int(input[0]), int(input[1]))

def is_contained(elf1, elf2):
    return elf1[0] <= elf2[0] and elf1[1] >= elf2[1]

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()