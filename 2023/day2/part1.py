def solution(lines, max_red=12, max_green=13, max_blue=14):
    sum = 0
    for line in lines:
        game = parse_game(line)
        if is_possible(game, max_red, max_green, max_blue):
            sum += game.id
            
    return sum

def is_possible(game,  max_red, max_green, max_blue) -> bool:
    for round in game.rounds:
        if round.red > max_red or round.green > max_green or round.blue > max_blue:
            return False
        
    return True

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