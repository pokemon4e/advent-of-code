import re

def solution(lines):
    sum = 0
    for line in lines:
        digits = [(i, int(x)) for i, x in enumerate(line) if x.isdigit()]
        digit_words = find_digit_words(line)
        all_digits = sorted(digits + digit_words, key= lambda x: x[0])
        sum += all_digits[0][1] * 10 + all_digits[-1][1]

    return sum

def find_digit_words(line):
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine))')
    return [(m.start(0), get_digit(m.group(1))) for m in re.finditer(pattern, line)]

def get_digit(word):
    match word:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9


def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()