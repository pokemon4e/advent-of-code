def bit_at_position(number, position):
    mask = 1 << position
    return int(number & mask > 0)

def common(position, numbers, default):
    ones_count = 0
    for n in numbers:
        ones_count += bit_at_position(n, position)

    threshold = len(numbers) / 2
    if ones_count == threshold:
        return default
    elif ones_count > threshold:
        return 1 if default == 1 else 0
    else:
        return 0 if default == 1 else 1

def get_rating(numbers, bit):
    position = 11
    while len(numbers) > 1:
        common_number = common(position, numbers, bit)
        numbers = [n for n in numbers if bit_at_position(n, position) == common_number]
        position -= 1
       
    return numbers[0]
    
def solution(numbers):
    oxygen_rating = get_rating(numbers, 1) 
    co2_rating = get_rating(numbers, 0)
    return oxygen_rating * co2_rating

def read_input(filename):
    with open(filename) as f:
        return [int(n, 2) for n in f.readlines()]
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()