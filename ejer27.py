
def move_game(player, game_board, avatar):

    error = False
    player = player.strip()
    player_list = player.split(',')

    # row and columns rest 1 because the player do not start in zero
    row = (int(player_list[0]) - 1) 
    column = (int(player_list[1]) - 1)

    if game_board[row][column] != 0:
        error = True
        return error

    else:
        game_board[row][column] = avatar
        return game_board
        


if __name__ == '__main__':
    
    game_board = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]

    while True:

        while error:
        player1 = input('What is the move player 1(row, column), example 2,3: ')
        game_board = move_game(player1, game_board, 'X')
        print(game_board)

        player2 = input('What is the move player 2(row, column), example 2,3: ')
        game_board = move_game(player2, game_board, 'O')
        print(game_board)
        
        
