from collections import defaultdict

def solution(numbers, days):
    fish_counter_by_day = defaultdict(int)
    for n in numbers:
        fish_counter_by_day[n] += 1

    while days > 0:
        new_fish_counter_by_day = defaultdict(int)
        new_fish_counter_by_day[8] += fish_counter_by_day[0] # new fish
        new_fish_counter_by_day[6] += fish_counter_by_day[0] # new cycle for existing fish
        for age in range(1, 9):
            new_fish_counter_by_day[age - 1] += fish_counter_by_day[age]
            
        fish_counter_by_day = new_fish_counter_by_day
        days -= 1
            
    return sum(fish_counter_by_day.values())

def read_input(filename):
    with open(filename) as f:
        return [int(n) for n in f.readline().split(',')]
    
def main():
    print(solution(read_input('input.txt'), 256))

if __name__ == "__main__":
    main()