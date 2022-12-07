def solution(lines):
    sum = 0
    
    for line in lines:
        sum += calc_line(line)
    
    return sum

def calc_line(line):
    input = sorted(line.split(','))
    elves = sorted([get_elf_section(input[0]), get_elf_section(input[1])])
    
    if is_overlap(elves[0], elves[1]):
        return 1
    else:
        return 0
    
def get_elf_section(elf):
    input = elf.split('-')
    
    return (int(input[0]), int(input[1]))

def is_overlap(elf1, elf2):
    return elf2[0] <= elf1[1]

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()