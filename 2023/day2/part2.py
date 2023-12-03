def solution(lines, max_red=12, max_green=13, max_blue=14):
    sum = 0
    for line in lines:
        game = parse_game(line)
        min_red, min_green, min_blue = get_min_to_be_possible(game)
        sum += min_red * min_green * min_blue
            
    return sum

def get_min_to_be_possible(game):
    min_red = min_green = min_blue = 0
    for round in game.rounds:
        min_red = max(min_red, round.red)
        min_green = max(min_green, round.green)
        min_blue = max(min_blue, round.blue)
        
    return (min_red, min_green, min_blue)

def parse_game(line: str):
    groups = line.split(':')

    id = int(groups[0].split(' ')[1])    
    rounds = [parse_round(round) for round in groups[1].split(';') if round.strip()]

    return Game(id, rounds)

def parse_round(round_str: str):
    round = Round()

    cubes = round_str.split(',')
    for cube in cubes:
        groups = [group.strip() for group in cube.split(' ') if group]
        quantity = int(groups[0])  
        match groups[1]:
            case 'red':
                round.red += quantity
            case 'green':
                round.green += quantity
            case 'blue':
                round.blue += quantity
    return round

class Game:
    def __init__(self, id: int, rounds: list) -> None:
        self.id = id
        self.rounds = rounds

class Round:
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.red = red
        self.green = green
        self.blue = blue

def read_input(filename):
    with open(filename) as f:
        return f.readlines()
    
def main():
    print(solution(read_input('input.txt')))

if __name__ == "__main__":
    main()