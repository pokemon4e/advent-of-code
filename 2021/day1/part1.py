def solution(numbers):
    counter = 0
    for i, n in enumerate(numbers):
        if i > 0 and n > numbers[i - 1]:
            counter += 1
        
    return counter
    
def read_input(filename):
    with open(filename) as f:
        return [int(n) for n in f.readlines()]
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()