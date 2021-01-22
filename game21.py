import random


def ace(x, s):
    summ = 0
    s["Туз"] = 1
    for el in x:
        rank1 = el.split()
        summ += s[rank1[0]]
    return summ


def new_card(deal, sum1, desk1):
    score = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, "Валет": 2, "Дама": 3, "Король": 4, "Туз": 11}
    rank2 = desk1.split()
    sum1 += score[rank2[0]]
    if sum1 > 21 and (('Туз крести' in deal) or ('Туз буби' in deal) or ('Туз вини' in deal) or ('Туз черви' in deal)):
        sum1 = ace(deal, score)
    return sum1


def error_answer(answer2):
    if answer2.lower().strip(" ") == 'да' or answer2.lower().strip(" ") == 'нет':
        return False
    else:
        return True


def answer(answer1):
    while error_answer(answer1):
        print('Ошибка ввода!')
        answer1 = input('''(Введите да/нет)
''')
    if answer1.lower().strip(" ") == 'да':
        return True
    else:
        return False


def win(sumg, sumd):
    if sumg == 21:
        print('Ваша победа! У вас очко)0)')
        return True
    elif sumg > 21:
        print('Победа дилера! У вас перебор :(')
        return True
    elif sumd == 21:
        print('Победа дилера! У него очко)0)')
        return True
    elif sumd > 21:
        print('''Ваша победа! У дилера перебор)
Сумма ваших очков: {0} 
Сумма очков дилера: {1}'''.format(sumg, sumd))
        return True
    else:
        return False


def new_game():
    suits = ["крести", "буби", "вини", "черви"]
    ranks = ['6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
    new_desk = []
    for suit in suits:
        for rank in ranks:
            new_desk.append(rank + " " + suit)
    random.shuffle(new_desk)
    return new_desk


def first_delivery(desk0):
    sum_g = 0
    sum_d = 0
    deal_g1 = desk0.pop()
    deal_d1 = desk0.pop()
    sum_g = new_card(deal_g1, sum_g, deal_g1)
    sum_d = new_card(deal_d1, sum_d, deal_d1)
    return sum_d, sum_g, deal_g1, deal_d1, list(desk0)



def count(sum_ga, sum_de):
    print('Подсчёт очков...')
    if sum_ga > sum_de:
        print('''Ваша победа! 
    Сумма ваших очков: {0} 
    Сумма очков дилера: {1}'''.format(sum_ga, sum_de))
    elif sum_de > sum_ga:
        print('''Победа дилера! 
    Сумма ваших очков: {0} 
    Сумма очков дилера: {1}'''.format(sum_ga, sum_de))
    else:
        print('Ничья! Сумма ваших очков равна сумме очков дилера')


desk = list(new_game())
sum_dealer, sum_gamer, deal_gamer_1, deal_dealer_1, desk = first_delivery(desk)
deal_gamer = [deal_gamer_1]
deal_dealer = [deal_dealer_1]
n = True
while n:
    deal_gamer.append(desk.pop())
    deal_dealer.append(desk.pop())
    sum_gamer = new_card(deal_gamer, sum_gamer, deal_gamer[-1])
    sum_dealer = new_card(deal_dealer, sum_dealer, deal_dealer[-1])
    print('''Ваши карты: 
{0} 
Сумма очков: 
{1}'''.format(deal_gamer, sum_gamer))
    if win(sum_gamer, sum_dealer):
        answer_new_game = input('''
Начать новую игру? 
(Введите да/нет)
''')
        if answer(answer_new_game):
            desk = list(new_game())
            sum_dealer, sum_gamer, deal_gamer_1, deal_dealer_1, desk = first_delivery(desk)
            deal_gamer = [deal_gamer_1]
            deal_dealer = [deal_dealer_1]
            continue
    else:
        answer_new_card = input('''Хотите взять еще одну карту? 
(Введите да/нет)
 ''')
        if answer(answer_new_card):
            continue
        else:
            count(sum_gamer, sum_dealer)
            answer_new_game = input('''
Начать новую игру? 
(Введите да/нет)
''')
            if answer(answer_new_game):
                desk = list(new_game())
                sum_dealer, sum_gamer, deal_gamer_1, deal_dealer_1, desk = first_delivery(desk)
                deal_gamer = [deal_gamer_1]
                deal_dealer = [deal_dealer_1]
                continue
            else:
                break
