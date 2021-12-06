bingo_numbers = []
bingo_boards = []
marked_bingo_boards = []


def read_input():
    with open('./input/day-4-input.txt') as file:
        line_number = 1
        outer_array_index = -1
        for line in file:
            if line_number == 1:
                line_number += 1
                list = line.split(",")
                for i in list:
                    bingo_numbers.append(int(i))
            elif line == '\n':
                bingo_boards.append([])
                marked_bingo_boards.append([])
                outer_array_index += 1
            else:
                bingo_boards[outer_array_index].append(
                    [int(x.strip() or '0') for x in line.split()])
                marked_bingo_boards[outer_array_index].append([False] * 5)


def check_for_bingo():
    for board_index, board in enumerate(marked_bingo_boards):
        if check_rows_for_bingo(board) == True:
            return board_index
        elif check_columns_for_bingo(board) == True:
            return board_index
    return 0


def check_rows_for_bingo(board):
    for row in board:
        if False in row:
            continue
        else:
            return True
    return False


def check_columns_for_bingo(board):
    column_index = 0
    row_index = 0
    while column_index < 5:
        column = []
        while row_index < 5:
            column.append(board[row_index][column_index])
            row_index += 1
        if False in column:
            row_index = 0
            column_index += 1
            continue
        else:
            return True
    return False


def mark_bingo_number(called_number):
    for board_index, board in enumerate(bingo_boards):
        for row_index, row_values in enumerate(board):
            for value_index, value in enumerate(row_values):
                if value == called_number:
                    marked_bingo_boards[board_index][row_index][value_index] = True


def calculate_final_score(board, index):
    sum = 0
    for row_index, row_values in enumerate(board):
        for value_index, value in enumerate(row_values):
            if value == False:
                sum += bingo_boards[index][row_index][value_index]
    return sum


def process_input():
    read_input()
    for bingo_number in bingo_numbers:
        mark_bingo_number(bingo_number)
        bingo_found_index = check_for_bingo()
        if bingo_found_index > 0:
            return calculate_final_score(marked_bingo_boards[bingo_found_index], bingo_found_index) * bingo_number


print(f'{process_input()}')
