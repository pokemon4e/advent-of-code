def bit_at_position(number, position):
    mask = 1 << position
    return int(number & mask > 0)

def solution(numbers):
    bits = 12
    ones_count = [0] * bits
    
    for n in numbers:
        for i in range(bits):
            if bit_at_position(n, i):
                ones_count[bits - i - 1] += 1

    gamma_rate = 0
    threshold = len(numbers) // 2
    for i in range(bits):
        if ones_count[bits - i - 1] > threshold:
            mask = 1 << i
            gamma_rate = gamma_rate | mask

    epsilon_rate = 0xFFF ^ gamma_rate
    return epsilon_rate * gamma_rate

def read_input(filename):
    with open(filename) as f:
        return [int(n, 2) for n in f.readlines()]
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()