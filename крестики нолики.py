fild = '*' * 9
fild = list(range(1, 10))


def make_fild(fild):
    print('-' * 12) # верхняя полоска
    for i in reversed(range(3)):
        print(f': {fild[0+i*3]} : {fild[1+i*3]} : {fild[2+i*3]} :') # двоеточие можно поменять на другой знак
        print('-' *12)


def take_input(igrok_token): # функция на проверку ввода нужного значка
    valid = False
    while not valid:
        igrok_answer = input(f'выберети место куда поставить {igrok_token}?')
        try:
            igrok_answer = int(igrok_answer) # преобразует строковую переменную в числовую
        except:
            print('Нужно ввести число от 1 до 9')
            continue
        if igrok_answer >= 1 and igrok_answer<=9:
            if (str(fild[igrok_answer-1]) not in 'XO'):
                fild[igrok_answer-1] = igrok_token
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Введите число от 1 до 9')

# ниже написана функция проверки выигрышной ситуации
def chek_win(fild):
    win_cord = ((0,1,2), (3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_cord:
        if fild[each[0]] == fild[each[1]] ==fild[each[2]]:
            return fild[each[0]]
    return False

# ниже написана функция которая управляет игровым процессом
def main(fild):
    counter = 0
    win = False
    while not win:
        make_fild(fild)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1

        if counter > 4:
            tmp = chek_win(fild)
            if tmp:
                print(tmp, 'Ты выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    make_fild(fild)


main(fild)