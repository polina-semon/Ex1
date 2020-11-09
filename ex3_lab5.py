from random import randint, choice

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


class Attacker:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack

    def experience(self, target):
        target._experience = self._experience + 25

    def is_alive(self):
        return self._health >= 0


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._name = 'зелёный дракон'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._name = 'красный дракон'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._name = 'черный дракон'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class TrollGuess(Dragon):
    def __init__(self):
        self._health = 0
        self._attack = 0
        self._name = 'тролль-угадайка'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest


class PrimeTroll(Dragon):
    def __init__(self):
        self._health = 0
        self._attack = 10
        self._name = '"простой" тролль'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Простое ли это число ' + str(x) + '? Напишите 1, если число простое и 0 в противном случае.'
        if x in prime_numbers:
            self.set_answer(1)
        else:
            self.set_answer(0)
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, TrollGuess, PrimeTroll]


class Hero(Attacker):
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._attack = 50
        self._experience = 0


def annoying_input_int(message=''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Ваш противник -', dragon._name + '!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ: ')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                hero.experience(hero)
                print('Верно! \n** противник кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print(dragon._name, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')


def start_game():
    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())

        dragon_number = 5
        dragon_list = generate_dragon_list(dragon_number)
        assert (len(dragon_list) == 5)
        print('У Вас на пути', dragon_number, 'врагов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')


print(__name__)

if __name__ == '__main__':
    start_game()