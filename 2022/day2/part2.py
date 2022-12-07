possible_actions = ['rock', 'paper', 'scissors']
win_actions = ['paper', 'scissors', 'rock']
lose_actions = ['scissors', 'rock', 'paper']

def solution(lines):
    sum = 0
    
    for line in lines:
        sum += calc_round(line)
    
    return sum

def calc_round(line):
    input = line.split(' ')
    opponent = input[0].strip()
    outcome = input[1].strip()
    
    opponent_index = ord(opponent) - ord('A')
    action = possible_actions[opponent_index]
    
    outcome_index = ord(outcome) - ord('X')
    if outcome_index == 0:
        action = lose_actions[opponent_index]
    elif outcome_index == 2:
        action = win_actions[opponent_index]

    return outcome_index * 3 + possible_actions.index(action) + 1

    
def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()