def solution(lines):
    n = len(lines)
    sum = 0
    for i in range(n):
        prev = lines[i - 1] if i - 1 >= 0 else None
        next = lines[i + 1] if i + 1 < n else None 
        sum += find_numbers(lines[i], prev, next)  
    
    return sum        
    
def find_numbers(line: str, prev_line: str, next_line: str):
    sum = 0
    current_number = ''
    start_index = end_index = 0
    
    for i, c in enumerate(line):
        if c.isdigit():
            current_number += c
            end_index += 1
        else:
            if current_number and is_valid(line, prev_line, next_line, start_index, end_index - 1):
                print(f'Found a valid number: {current_number}')
                sum += int(current_number)
            current_number = '' 
            start_index = end_index = i + 1
    
    return sum
    

def is_valid(line: str, prev_line: str, next_line: str, start_index: int, end_index: int):
    print(f'Checking line: {line}, start_index {start_index}, end_index {end_index}')
    # Check line
    if contains_symbols(line, start_index, end_index):
        print(f'Current line contains symbol')
        return True

    # Check prev line
    if prev_line and contains_symbols(prev_line, start_index, end_index):
        print(f'Prev line contains symbol')
        return True

    # Check next line
    if next_line and contains_symbols(next_line, start_index, end_index):
        print(f'Next line contains symbol')
        return True
    
    return False

def contains_symbols(line: str, start_index, end_index):
    start = max(0, start_index - 1)
    end = min(len(line), end_index + 2) # exclusive 
    for i in range(start, end):
        if is_symbol(line[i]):
            print(f'Found symbol: {line[i]}')
            return True
    
    return False  
        
def is_symbol(char: str):
    return char != '.' and not char.isdigit()

def read_input(filename: str):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()