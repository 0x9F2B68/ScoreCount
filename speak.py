import os
from random import randint


# SCORECOUNT    ver.1.1
# pooh gamedev studio montreal (dzr1380)
# TΔkeshį Øreö ©


# функция определяющая уровень сложности
# возвращает число, между которым будет считаться рандом
def lvl():
    print("Choose. Your. Destiny.")
    
    difficulty = input("\nВыбери уровень сложности:\n1) Изи пизи\n2) Лемон сквизи\n3) Мазафакер\n")
    if difficulty == "1":
        return 20
    elif difficulty == "2":
        return 99
    elif difficulty == "3":
        return 999
    else:
        print("Ты дурачок что-ли?")
        return 999999


# функция считающая кол-во очков в зависимости от ответа/неответа
def count_score(mistake, difficulty):  # зададки на норм счетчик
    if mistake:
        if difficulty == 20:
            return -1
        elif difficulty == 99:
            return -3
        elif difficulty == 999:
            return -27
        else:
            return 0
    if not mistake:
        if difficulty == 20:
            return 1
        elif difficulty == 99:
            return 3
        elif difficulty == 999:
            return 27
        else:
            return 0


# функция для сохранения лидерборда в программе (два списка) в порядке убывания
def ScoreBoard_lists():
    file = open("scoreboard.txt", "r")
    leaders = []
    points = []
    for i in file:  # из файла в массивы
        tmp2_ldrs = 0  # для счета откуда считать строку для leaders
        pnts, ldrs = "", ""
        for j in i:
            if j != "|":
                pnts += j
                tmp2_ldrs += 1
            else:
                break
        points.append(pnts)
        for j in i:
            if j != "\n":
                ldrs += j
            else:
                break
        tmp2_ldrs += 1
        tmp_ldrs = ldrs[tmp2_ldrs:]
        leaders.append(tmp_ldrs)
    points.reverse()
    leaders.reverse()
    file.close()
    return points, leaders


# функция которая делает ДОСКУ ДОСТИЖЕНИЙ
# 6 ЧАСОВ ДЕЛАЛ АААААА
# работет на костылях
# мб когда нибудь сделаю нормально
# (если смогу)
def ScoreBoard_insert(score):
    with open('scoreboard.txt', 'r') as file:
        tmp = ""
        check = file.readline()
        for i in check:  # рекорд ли это?
            if i != "|":
                tmp += i
            else:
                break
    
    # нужно ли вообще добавлять рекорд
    if int(tmp) < score:  # сравниваем с 1 потому что по возрастанию
        name = input("Введи свое имя: ")
        points, leaders = ScoreBoard_lists()
        # сортировка массива с новым значением
        for i in range(0, 10):
            if score > int(points[i]):
                points.pop()
                leaders.pop()
                points.insert(i, score)
                leaders.insert(i, name)
                break
        points.reverse()
        leaders.reverse()
        with  open("scoreboard.txt", "w") as file:  # из массивов в файл
            for i in range(0, 10):
                file.write(f"{ str(points[i]) },{ leaders[i] }\n")


# функция чисто показывает на экран доску
def ScoreBoard_show():
    points, leaders = ScoreBoard_lists()
    print("################################################")  # 46 #
    print("#________________ДОСКА__ПОЧЕТА!________________#")
    str = ""
    tmp = 0
    for i in range(0, 10):
        tmp = 46 - (len(leaders[i]) + 4 + len(points[i]))
        str = "# " + leaders[i]
        for j in range(0, (tmp)):
            str += "_"
        str = str + points[i] + " #"
        print(str)
    print("################################################")


# основная функция которая подразумевает под собой игру
def game(hardcore, num):
    HP = 1
    exit = True
    score = 0
    while exit:
        a = randint(0, num)
        b = randint(0, num)
        print(f"Сколько будет {a} + {b}?")
        try:
            answer = int(input())
            if answer == a + b:
                print("Nice")
                if hardcore:
                    score += count_score(False, num)  # считает очки
                    print(f"Score = {score}")
                    print(f"Health = {HP}")
                else:
                    score += 1  # считает количество ходов
            else:
                if HP != 0:
                    print("Try again")
                    if hardcore:
                        score += count_score(True, num)  # считает очки
                        HP -= 1
                        print(f"Score = {score}")
                        print(f"Health = {HP}")
                    else:
                        score += 1  # считает количество ходов
                else:
                    print("Game over")
                    exit = False
        except ValueError:
            print("Не поняла")
    print("Ваш результат: ", score)
    if score <= 0:
        print("Неудача")
    return score


def main():
    print("##############################################")  # 46 #
    # talk(" Добро пожаловать в SCORE COUNT!")
    print(" Ver 1.1")
    print(" Меню:\n 1) Выживание\n 2) Аркада\n 3) Настройки\n 4) Лидерборд")
    print("##############################################")  # 46 #
    try:
        choose = input("Insert coin: ")
        if choose == "1":
            # talk("Я пришла сыграть с тобой в игру")
            # talk("тут должна начаться главная тема из пилы")
            # talk("сегодня ты будешь у меня считать")
            # talk("Начнем пожалуй, ты готов?")
            # talk("Prepare to battle")
            num = lvl()  # что бы выбрать уровень
            score = game(True, num)
            ScoreBoard_insert(score)
            ScoreBoard_show()

        elif choose == "2":
            print("Let's go!")
            num = 99
            game(False, num)

        # elif choose == "3":
        # settings
        elif choose == "4":
            ScoreBoard_show()
    except ValueError:
        print("Не поняла")


if __name__ == "__main__":
    main()