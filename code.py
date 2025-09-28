# Правила игры следующие. На шахматной доске в некоторых клетках случайно разбросаны фишки или пуговицы.
# Игроки ходят по очереди. За один ход можно снять все фишки с какой-либо горизонтали или вертикали, на которой они есть.
# Выигрывает тот, кто заберет последние фишки

import random #импортирую библиотеку рандом для заполнения фишек на поле

size = 8
board = [] #массив для заполнения макета доски фишками
for i in range(size):
    row = []
    for j in range(size):
        if random.randint(0, 1) == 1:
            row.append(1)
        else:
            row.append(0)
    board.append(row)

def print_board(): #функция которая будет выводит доску заполненую фишками на данный момент
    print("―" * 34)
    print("│ h╲v │ ", end=" ")
    for colm in range(size):
        print(colm + 1, end="  │  ")
    print()
    print("―" * 34)
    for row in range(size):
        print("│ " + str(row + 1).rjust(2), end="  │ ")
        for colm in range(size):
            if board[row][colm] == 1:
                print(" ◯ ", end=" │ ")
            else:
                print("   ", end=" │ ")
        print()
        print("―" * 34)

def clear_line(colm, num): #функция для очищения ряда или колонки от фишек т.е. ход человека
    if colm == "h":
        row = num - 1

        found = False #переменная которая будет показывать есть ли в данной строке или столбце фишки

        for colm in range(size): #если есть хотя бы одна фишка ход будет возможен
            if board[row][colm] == 1:
                found = True
                break

        if not found: #ну а если нет фишек то ход невозможен
            return False

        for colm in range(size): #убираем фишки с доски
            board[row][colm] = 0

        return True #если ход был совершен успешно функция выполняется

    elif colm == "v": #аналогично для вертикали
        col = num - 1

        found = False

        for roww in range(size):
            if board[roww][col] == 1:
                found = True
                break

        if not found:
            return False

        for roww in range(size):
            board[roww][col] = 0

        return True

def have_chips(): # функция проверяющая остались ли еще фишки на доске
    for row in board:
        for chip in row:
            if chip == 1:
                return True
    return False

print("Игра Супер Ним") #приветствие и ввод имени первого игрока
print("\033[1m\033[32m{}\033[0m".format("Правила игры следующие. На шахматной доске в некоторых клетках случайно разбросаны фишки или пуговицы."))
print("\033[1m\033[32m{}\033[0m".format("Игроки ходят по очереди. За один ход можно снять все фишки с какой-либо горизонтали или вертикали, на которой они есть."))
print("\033[1m\033[32m{}\033[0m".format("Выигрывает тот, кто заберет последние фишки"))

while True:
    player1 = input("Введите имя игрока 1: ").strip()
    if player1 == "":
        print("\033[1m\033[31m{}\033[0m".format("Имя некорректно"))
    else:
        break

while True: #ввод имени игрока номер 2
    player2 = input("Введите имя игрока 2: ").strip()
    if player2 == "":
        print()
        print("\033[1m\033[31m{}\033[0m".format("Имя некорректно"))
        print()
    else:
        break

current = player1 #это будет переменной показывающей имя игрока, чей сейчас ход

print_board() #выводим доску
while True:
    print("h = горизонталь, v = вертикаль") #предоставляем право хода и показываем пример входных данных
    print(f"{current}, ваш ход")
    move = input("Введите координаты через пробел (пример: h 3): ").split()

    if len(move) != 2: #проверка на корректность введенных данных(напрмер пустая строка)
        print()
        print("\033[1m\033[31m{}\033[0m".format("Неправильный ввод"))
        print()
        continue

    tip = move[0] #проверка на корректность ряда или колонки с учетом того, что пользователь ввел заглавную букву или не поменял раскладку клваиатуры или ввел на русском
    k = tip.lower()
    if k in ("h", "р", "г"):
        tip = "h"
    elif k in ("v", "м", "в"):
        tip = "v"
    else:
        print()
        print("\033[1m\033[31m{}\033[0m".format("Неправильный тип линии (h или v)"))
        print()
        continue

    try: #трай для того чтобы проверить второй символ на принадлежность к типу инт и избегание ошибки в случае иначе
        num = int(move[1])
    except:
        print()
        print("\033[1m\033[31m{}\033[0m".format("Введите целое число вторым символом"))
        print()
        continue

    if num < 1 or num > size: #проверка на корректность номера столбца или строки
        print()
        print("\033[1m\033[31m{}\033[0m".format("Некорректный номер"))
        print()
        continue

    hod = clear_line(tip, num)

    if not hod: #если функция вернула фолз то фишек нет и ход некорректный
        print()
        print("\033[1m\033[31m{}\033[0m".format("Там нет фишек"))
        print()
        continue

    if not have_chips(): #проверяем остались ли фишки на доске(уловие победы)
        print_board()
        print()
        print("\033[1m\033[32m{}\033[0m".format("Победил"), current)
        break #окончание игры победа текущего игрока

    if current == player1: #смена хода игрока
        current = player2
        print()
        print()
        print_board()
    else:
        current = player1
        print()
        print()
        print_board()