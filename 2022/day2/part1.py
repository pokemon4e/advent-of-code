possible_actions = ['rock', 'paper', 'scissors']
win_actions = ['paper', 'scissors', 'rock']

def solution(lines):
    sum = 0
    
    for line in lines:
        sum += calc_round(line)
    
    return sum

def calc_round(line):
    input = line.split(' ')
    opponent = input[0].strip()
    player = input[1].strip()
    
    opponent_index = ord(opponent) - ord('A')
    player_index = ord(player) - ord('X')
    
    return player_index + 1 + get_score(opponent_index, player_index)
    

def get_score(opponent_index, player_index):
    if opponent_index == player_index:
        return 3 # draw
    
    if possible_actions[player_index] == win_actions[opponent_index]:
        return 6
    
    return 0

    
def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()