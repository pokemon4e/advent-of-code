from os import umask
from collections import defaultdict
import functools
import operator

class matrix:
    def __init__(self) -> None:
        self.__positions = []
        self.__marked_total_row = defaultdict(int)
        self.__marked_total_col = defaultdict(int)
        self.__unmarked_total = 0
        
    @property
    def positions(self) -> list:
        return self.__positions

    @property
    def unmarked_total(self) -> int:
        return self.__unmarked_total

    def add_number(self, number: int, row: int, col: int) -> None:
        self.__unmarked_total += number
        self.__positions.append(position(self, number, row, col))

    def mark_number(self, position) -> bool:
        self.__unmarked_total -= position.number
        row = position.row
        col = position.col
        self.__marked_total_row[row] += 1
        self.__marked_total_col[col] += 1
        return self.__marked_total_row[row] >= 5 or self.__marked_total_col[col] >= 5

class position:    
    def __init__(self, matrix: matrix, number: int, row: int, col: int) -> None:
        self.__matrix = matrix
        self.__number = number
        self.__row = row
        self.__col = col
        
    @property
    def matrix(self) -> matrix:
        return self.__matrix
    
    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def row(self) -> int:
        return self.__row
    
    @property
    def col(self) -> int:
        return self.__col
 

def solution(bingo_numbers, matrix_list):
    positions = [m.positions for m in matrix_list]
    flat_positions = functools.reduce(operator.iconcat, positions, [])
    position_list_by_number = defaultdict(list)
    
    for position in flat_positions:
        position_list_by_number[position.number].append(position)
    
    for number in bingo_numbers:
        for position in position_list_by_number[number]:
            m = position.matrix
            if m.mark_number(position):
               return number * m.unmarked_total
            

def read_input(filename):
    with open(filename) as f:
        bingo_numbers = [int(n) for n in f.readline().split(',')]
        f.readline() #empty line
        
        current_matrix_index = 0
        row = 0
        matrix_list = [matrix()]
        while line := f.readline():
            if not line.strip():
                current_matrix_index += 1
                row = 0
                matrix_list.append(matrix())
            else:
                for col, n in enumerate(line.split()):
                    matrix_list[current_matrix_index].add_number(int(n), row, col)
            
                row += 1
                
    return bingo_numbers, matrix_list
    
def main():
    print(solution(*read_input('input.txt')))

if __name__ == "__main__":
    main()