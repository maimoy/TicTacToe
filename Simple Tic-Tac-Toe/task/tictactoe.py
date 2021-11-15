# write your code here

upper_line = "-" * 11
bottom_line = "-" * 11
line1 = []
line2 = []
line3 = []
game_board = {}
win_player_x = False
win_player_o = False
game_is_draw = False


def draw_board(input_string):
    line1 = list(input_string[0:3])
    line2 = list(input_string[3:6])
    line3 = list(input_string[6:9])
    print(upper_line)
    print("| " + " ".join(line1)+" |")
    print("| " + " ".join(line2)+" |")
    print("| " + " ".join(line3)+" |")
    print(bottom_line)


def check_state(l1, l2, l3):
    game_list = [l1, l2, l3]
    count_plays = l1.count("_")
    count_plays += l2.count("_")
    count_plays += l3.count("_")


def create_game_board():
    for i in range(9):
        game_board[i] = "_"


def fill_game_bord_from_input(input_string):
    for i in range(9):
        game_board[i] = input_string[i]


def check_for_win(char_to_check):
    if game_board[0] == char_to_check and game_board[1] == char_to_check and game_board[2] == char_to_check:
        return True
    elif game_board[3] == char_to_check and game_board[4] == char_to_check and game_board[5] == char_to_check:
        return True
    elif game_board[6] == char_to_check and game_board[7] == char_to_check and game_board[8] == char_to_check:
        return True
    elif game_board[0] == char_to_check and game_board[3] == char_to_check and game_board[6] == char_to_check:
        return True
    elif game_board[1] == char_to_check and game_board[4] == char_to_check and game_board[7] == char_to_check:
        return True
    elif game_board[2] == char_to_check and game_board[5] == char_to_check and game_board[8] == char_to_check:
        return True
    elif game_board[0] == char_to_check and game_board[4] == char_to_check and game_board[8] == char_to_check:
        return True
    elif game_board[2] == char_to_check and game_board[4] == char_to_check and game_board[6] == char_to_check:
        return True
    else:
        return False


def check_for_draw():
    count_empty_places = 0
    count_x = 0
    count_o = 0
    for i in range(9):
        if game_board[i] == '_':
            count_empty_places += 1
    if count_empty_places > 0:
        return False
    else:
        return True


def check_for_error_plays():
    count_x = 0
    count_o = 0
    for i in range(9):
        if game_board[i] == 'X':
            count_x += 1
        if game_board[i] == 'O':
            count_o += 1
    if abs(count_o - count_x) > 1:
        return True
    else:
        return False


def check_user_input(input):
    try:
        value = int(input)
        return True
    except ValueError:
        try:
            value = float(input)
            return True
        except ValueError:
            print("You should enter numbers!")
            return False


def check_for_valid_input(x, y):
    if 0 < x <= 3:
        if 0 < y <=3:
            return True
        else:
            return False
    else:
        return False


def draw_new_state(x_cor, y_cor):
    global is_player_x_turn
    if is_player_x_turn:
        game_board[(((y_cor - 1) * 3) + (x_cor-1))] = 'X'
        is_player_x_turn = not is_player_x_turn
    else:
        game_board[(((y_cor - 1) * 3) + (x_cor - 1))] = 'O'
        is_player_x_turn = not is_player_x_turn
    string_from_gameboard = ""
    list_from_gameboard = list(game_board)
    results_from_gameboard = ""
    for k in list_from_gameboard:
        results_from_gameboard += game_board[k]
    global user_input
    user_input = results_from_gameboard
    draw_board(results_from_gameboard)


def check_for_occupied(x, y):
    if game_board[(((y - 1) * 3) + (x-1))] == '_':
        return True
    else:
        # print("This cell is occupied! Choose another one!")
        return False


entered = False
game_finished = False
user_input = "_________"
is_player_x_turn = True
create_game_board()
draw_board(user_input)

while not game_finished:
    # print("Enter cells: ")
    # user_input = input()
    # print(game_board)
    # create_game_board()
    # print(game_board)
    # draw_board(user_input)
    print("Enter the coordinates:")
    string_coords = input()
    entered = False
    while not entered:
        fill_game_bord_from_input(user_input)
        # print("Enter the coordinates:")
        # string_coords = input()
        if len(string_coords.split(" ")) != 2:
            print("You should enter numbers!")
            entered = True
            continue
        y_coordinate, x_coordinate = string_coords.split(" ")
        if check_user_input(x_coordinate):
            if check_user_input(y_coordinate):
                x_coordinate = int(x_coordinate)
                y_coordinate = int(y_coordinate)
            else:
                entered = True
                continue

        else:
            entered = True
            continue

        if check_for_valid_input(x_coordinate, y_coordinate):
            check_for_occupied(x_coordinate, y_coordinate)
        else:
            print("Coordinates should be from 1 to 3!")
            entered = True
            continue

        if check_for_occupied(x_coordinate, y_coordinate):
            # print("correct")
            draw_new_state(x_coordinate, y_coordinate)
            entered = True
            # game_finished = True
        else:
            entered = True
            print("This cell is occupied! Choose another one!")

    win_player_x = check_for_win('X')
    win_player_o = check_for_win('O')
    if win_player_o and win_player_x:
        print("Impossible")
    elif win_player_x:
        print("X wins")
        game_finished = True
    elif win_player_o:
        print("O wins")
        game_finished = True
    else:
        has_errors = check_for_error_plays()
        game_is_draw = check_for_draw()
        if not has_errors:
            if game_is_draw:
                print("Draw")
                game_finished = True
            else:
                game_finished = False
                # print("Game not finished")
        else:
            print("Impossible")




'''
win_player_x = check_for_win('X')
win_player_o = check_for_win('O')
if win_player_o and win_player_x:
    print("Impossible")
elif win_player_x:
    print("X wins")
elif win_player_o:
    print("O wins")
else:
    has_errors = check_for_error_plays()
    game_is_draw = check_for_draw()
    if not has_errors:
        if game_is_draw:
            print("Draw")
        else:
            print("Game not finished")
    else:
        print("Impossible")
'''
