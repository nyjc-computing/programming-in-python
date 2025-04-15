import random

GRID_SIZE = 10
EMPTY = "~"
HIT = "X"
MISS = "O"

HORIZONTAL = "horizontal"
VERTICAL = "vertical"


def create_grid(n: int, char: str) -> "list[list[str]]":
    """Create a grid of size n x n filled with char, and return it."""
    grid = []
    for _ in range(n):
        grid.append([char] * n)
    return grid

def is_unoccupied(board: "list[list[str]]", row: int, col: int, size: int, orientation: str) -> bool:
    """Check if the specified area on the board is unoccupied.

    Return True if unoccupied, False otherwise.
    """
    if orientation == HORIZONTAL:
        for i in range(size):
            if board[row][col + i] != EMPTY:
                return False
    elif orientation == VERTICAL:
        for i in range(size):
            if board[row + i][col] != EMPTY:
                return False
    return True

def place_ship_horizontally(board: "list[list[str]]", ship_name: str, size: int, row: int, col: int) -> None:
    """Place a ship horizontally on the board at the specified location.

    Return True if successful, False if not.

    Carry out validation first to check that the ship fits in the specified location and that the space is empty.
    """
    for i in range(size):
        board[row][col + i] = ship_name

def place_ship_vertically(board: "list[list[str]]", ship_name: str, size: int, row: int, col: int) -> None:
    """Place a ship vertically on the board at the specified location.

    Return True if successful, False if not.

    Carry out validation first to check that the ship fits in the specified location and that the space is empty.
    """
    for i in range(size):
        board[row + i][col] = ship_name

def place_ship(board: "list[list[str]]", ship_name: str, size: int) -> None:
    """Place a ship of size size on the board at a random location."""
    orientation = random.choice([HORIZONTAL, VERTICAL])
    placed = False
    while not placed:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if orientation == HORIZONTAL and col + size <= GRID_SIZE:
            if is_unoccupied(board, row, col, size, HORIZONTAL):
                place_ship_horizontally(board, ship_name, size, row, col)
                placed = True
        elif orientation == VERTICAL and row + size <= GRID_SIZE:
            if is_unoccupied(board, row, col, size, VERTICAL):
                place_ship_vertically(board, ship_name, size, row, col)
                placed = True

def display_board(board: "list[list[str]]") -> None:
    """Display the current state of the board."""
    # Column label row
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    # Row label followed by the row contents
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def is_valid_guess(board: "list[list[str]]", text: str) -> bool:
    """Check if the guess is valid. Return True if valid, False otherwise.

    A guess is expected in the form "row,col", where row and col are integers between 0 and GRID_SIZE - 1.
    The guess is valid if the coordinates are within the bounds of the board and the cell has not been
    guessed before (not HIT or MISS).
    """
    if text.count(",") != 1:
        return False
    first, second = text.split(",")
    if not first.isdigit() or not second.isdigit():
        return False
    x, y = int(first), int(second)
    if not ((0 <= x < GRID_SIZE) and (0 <= y < GRID_SIZE)):
        return False
    if board[x][y] in (HIT, MISS):
        return False
    return True

def guess_to_coordinates(guess: str) -> "tuple[int, int]":
    """Convert a guess string to coordinates.

    Return the row and column as a tuple of integers.
    """
    first, second = guess.split(",")
    x, y = int(first), int(second)
    return x, y

def prompt_valid_guess(board: "list[list[str]]") -> "tuple[int, int]":
    """Prompt the user for a valid guess.

    If the guess is invalid, keep prompting until a valid guess is entered.

    Return the row and column of the guess, as a tuple.
    """
    guess = input("Enter your guess (row,col): ")
    while not is_valid_guess(board, guess):
        guess = input("Invalid guess. Enter your guess (row,col): ")
    return guess_to_coordinates(guess)

def get_enemy_guess(board: "list[list[str]]") -> "tuple[int, int]":
    """Generate a random guess for the enemy.

    Return the row and column of the guess, as a tuple.
    """
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    while board[x][y] in (HIT, MISS):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
    return x, y

def is_target_hit(board: "list[list[str]]", x: int, y: int) -> bool:
    """Check if the target hit a ship. Return True if it did, False otherwise."""
    return board[x][y] != EMPTY

def targetting_update(board: "list[list[str]]", hit_what: str, x: int, y: int) -> None:
    """Update the targetting board with the guess."""
    if hit_what == EMPTY:
        board[x][y] = MISS
    else:
        board[x][y] = HIT

def player_update(board: "list[list[str]]", x: int, y: int) -> None:
    """Update the player board with the guess."""
    if board[x][y] == EMPTY:
        board[x][y] = MISS
    else:
        board[x][y] = HIT

def is_won(hits: int, total_ship_cells: int) -> bool:
    """Check if the player has won. Return True if they have, False otherwise."""
    return hits == total_ship_cells

def is_gameover(turns: int, player_hits: int, enemy_hits: int, total_ship_cells: int) -> bool:
    """Check if the game is over. Return True if it is, False otherwise."""
    if is_won(player_hits, total_ship_cells) or is_won(enemy_hits, total_ship_cells):
        return True
    if turns <= 0:
        return True
    return False

def display_overlay(targetting: "list[list[str]]", playing: "list[list[str]]") -> None:
    """Display the targetting overlaid on the ship board."""
    # Column label row
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    # Row label followed by the row contents
    for i in range(GRID_SIZE):
        print(f"{i} ", end="")
        for j in range(GRID_SIZE):
            if targetting[i][j] == HIT:
                print(HIT, end=" ")
            elif targetting[i][j] == MISS:
                print(MISS, end=" ")
            else:
                print(playing[i][j], end=" ")
        print()  # end the row

def run_game(turns: int, ships: "dict[str, int]") -> None:
    # Variables for tracking game state
    player_hits = 0
    enemy_hits = 0
    total_ship_cells = sum(ships.values())

    # Data structures for tracking game data
    # For tracking player ships and damage
    player_board = create_grid(10, " ")
    player_ship_cells = {}  # To track each ship’s remaining cells
    player_targetting = create_grid(10, " ")  # For tracking player guesses and hits
    player_sunk_ships = []

    # Similarly for the enemy
    enemy_board = create_grid(10, " ")
    enemy_ship_cells = {}
    enemy_targetting = create_grid(10, " ")
    enemy_sunk_ships = []

    # Place ships on the boards
    for name, size in ships.items():
        place_ship(player_board, name, size)
        player_ship_cells[name] = size
        place_ship(enemy_board, name, size)
        enemy_ship_cells[name] = size

    while not is_gameover(turns, player_hits, enemy_hits, total_ship_cells):
        print("\nTurns left:", turns)
        print("\nPlayer's turn")
        display_board(player_targetting)
        x, y = prompt_valid_guess(player_targetting)

        hit_char = enemy_board[x][y]
        targetting_update(player_targetting, hit_char, x, y)
        if is_target_hit(enemy_board, x, y):
            player_hits += 1
            enemy_ship_cells[hit_char] -= 1
            if enemy_ship_cells[hit_char] == 0:
                print("You sunk the", hit_char + "!")
                player_sunk_ships.append(hit_char)
        print("Ships sunk:", " ".join(player_sunk_ships) or "None")

        print("\nEnemy's turn")
        x, y = get_enemy_guess(player_board)

        hit_char = player_board[x][y]
        targetting_update(enemy_targetting, hit_char, x, y)
        if is_target_hit(player_board, x, y):
            enemy_hits += 1
            player_ship_cells[hit_char] -= 1
            if player_ship_cells[hit_char] == 0:
                print("Enemy sunk the", hit_char + "!")
                enemy_sunk_ships.append(hit_char)
        display_overlay(enemy_targetting, player_board)
        print("Ships sunk:", " ".join(enemy_sunk_ships) or "None")
        turns -= 1

    # Game is over
    if player_hits == total_ship_cells:
        print("Congratulations! You sank all the enemy ships!")
        display_overlay(player_targetting, enemy_board)
    elif enemy_hits == total_ship_cells:
        print("Game over! The enemy sank all your ships!")
        display_overlay(enemy_targetting, player_board)
    else:
        print("Game over! You ran out of turns!")
        display_overlay(player_targetting, enemy_board)

if __name__ == "__main__":
    run_game(turns=30, ships={"B": 4, "C": 3, "D": 2})
