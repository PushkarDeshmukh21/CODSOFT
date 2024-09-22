import math

grid = [[' ' for _ in range(3)] for _ in range(3)]

def print_grid():
    for row in grid:
        print('|'.join(row))
        print('-' * 5)

def check_winner(grid):
    
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
            return grid[0][col]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return grid[0][2]

    return None

def is_grid_full(grid):
    return all(grid[row][col] != ' ' for row in range(3) for col in range(3))

def minimax(grid, depth, is_maximizing):
    winner = check_winner(grid)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_grid_full(grid):
        return 0

    if is_maximizing:
        high_score = -math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == ' ':
                    grid[row][col] = 'X'
                    score = minimax(grid, depth + 1, False)
                    grid[row][col] = ' '
                    high_score = max(score, high_score)
        return high_score
    else:
        high_score = math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == ' ':
                    grid[row][col] = 'O'
                    score = minimax(grid, depth + 1, True)
                    grid[row][col] = ' '
                    high_score = min(score, high_score)
        return high_score

def best_move():
    high_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'X'
                score = minimax(grid, 0, False)
                grid[row][col] = ' '
                if score > high_score:
                    high_score = score
                    move = (row, col)
    return move

def play_game():
    print("Tic-Tac-Toe Game!")
    print("You Play as O, AI plays as X.")
    human_turn = True

    while True:
        print_grid()
        if human_turn:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if grid[row][col] == ' ':
                grid[row][col] = 'O'
                if check_winner(grid):
                    print_grid()
                    print("You win!")
                    break
                human_turn = False
            else:
                print("Invalid move! Try again.")
        else:
            move = best_move()
            if move:
                grid[move[0]][move[1]] = 'X'
                if check_winner(grid):
                    print_grid()
                    print("AI wins!")
                    break
            else:
                print_grid()
                print("It's a draw!")
                break
            human_turn = True

play_game()
