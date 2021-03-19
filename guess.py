import random

# Игра "Угадай число"
# С помощью генератора случайных чисел выбирается число от 1 до 100
# Пользователю предлагается угадать заданное число.
# При каждой попытке, если число не равно заданному, програма сообщает больше оно или меньше введённого пользователем
# Если числа совпадают, то программа поздравляет с победой и сообщает количество попыток потребовавшихся для отгадывания

def endword(number):
    ''' Функция определяет правильное склонение слова "попытка"
    '''
    if number < 11:
        if number == 1:
            return 'попытка'
        if number in [2, 3, 4]:
            return 'попытки'
        if number > 4:
            return 'попыток'
    if number > 10 and number < 21:
        return 'попыток'
    if number > 20:
        x = int(str(number)[-1])
        if x == 0:
            return 'попыток'
        if x == 1:
            return 'попытка'
        if x in [2, 3, 4]:
            return 'попытки'
        if x > 4:
            return 'попыток'
    return 'попыток'

if __name__ == '__main__':
    random.seed()
    number_computer = random.randint(1, 100)
    number_user = 0
    number_attempts = 0

    print('Добро пожаловать в игру "Угадай число"')
    print('Компьютер загадывает число в диапазоне от 1 до 100.')
    print('Ваша задача угадать его за наименьшее количество попыток.')
    print('-' * 64)
    print('Если вы не хотите угадывать число введите любое значение меньше 0. Это приведёт к прекращению поиска и выходу из программы.')
    print('-' * 64)
    print('Число выбрано, угадывайте!')

    while number_user != number_computer:
        number_user = int(input('Ваш вариант? '))
        number_attempts += 1
        if number_user > number_computer:
            print('Больше, немного уменьшите.')
        if number_user < number_computer:
            print('Меньше, увеличьте.')
        if number_user == number_computer:
            print('ПОЗДРАВЛЯЮ! Вы угадалии, число {} правильный вариант.'.format(number_computer))
            print('Для поиска числа вам потребовалось {} {}.'.format(number_attempts, endword(number_attempts)))
        if number_user < 0:
            break

    print()
    print('-' * 64)
    input('Нажмите enter для выхода.')
