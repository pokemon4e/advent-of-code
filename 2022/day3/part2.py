def solution(lines):
    sum = 0
    
    for group in grouping(lines, 3):
        sum += calc_group(group)
    
    return sum

def grouping(iterable, n):
    return zip(*[iter(iterable)]*n)

def calc_group(group):
    item1_chars = get_char_set(group[0])
    item2_chars = get_char_set(group[1])
    
    item3 = group[2]
    for i in range(0, len(item3)):
        char = item3[i]
        if char in item1_chars and char in item2_chars:
            return get_char_value(char)
        
def get_char_value(char):
    ascii = ord(char)
    if ascii >= 97:
        return ascii - 96
    else:
        return ascii - 64 + 26
            
def get_char_set(str):
    chars = set()
    for i in range(0, len(str)):
        chars.add(str[i])
    
    return chars
    

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()