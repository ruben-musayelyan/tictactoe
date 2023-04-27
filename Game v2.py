# Игра крестики-нолики на Python
# ------------------------------
# Автор : Мусаелян Рубен


#? размер игрового поля 3x3
board_size = 3
#? ширина клетки в игре
cell_size = 4
#? цифры позиций игрового поля
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    '''Выводим игровое поле'''
    print('_' * cell_size * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') *3)
        print('',board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|') *3)
    pass

def game_step(index, char):
    '''Выполняем ход'''
    if index not in range(1,10) or board[index-1] in ('X','O'):
        return False
    
    board[index-1] = char
    return True
    

def check_win():
    '''Проверяем победу'''
    win = False
    #? кортеж победных комбинаций
    win_combination = (
        (0,1,2),(3,4,5),(6,7,8), # по горизонтали
        (0,3,6),(1,4,7),(2,5,8), # по вертикали
        (0,4,8),(2,4,6)          # по диагонали
    )

    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win
    

def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1

    draw_board()
    while (step < 10) and (check_win() == False):
        index = int(input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):'))
        
        if index == 0:
            break
        
        # если получилось счодить
        if game_step(index,current_player):
            print('Удачный ход')

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()

            # увеличим шаг если ход верный
            step += 1
        else:
            print('Неверный номер! Повторите ход!')
    if step == 10:
        print('Ничья')
    else:
        print('Выиграл ' + check_win())

        

    pass




print('Добро пожаловать в крестикиьнолики!')
start_game()

