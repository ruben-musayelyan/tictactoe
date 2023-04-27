#? размер игрового поля 3x3
board_size = 3
#? ширина клетки в игре
cell_size = 3
#? цифры позиций игрового поля
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    '''Выводим игровое поле'''
    print(('_' * cell_size + ' ') * board_size)

    for i in range(board_size):

        print((' ' * board_size + '|') *board_size)

        print('', board[i*board_size], '|', board[1 + i*board_size], '|', board[2 + i*board_size], '|')

        print(('_' * board_size + '|') * board_size)

draw_board()