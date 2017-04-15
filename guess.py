# -*- coding:utf-8 -*-

# Игра "Угадай число"
# С помощью генератора случайных чисел выбирается число от 1 до 100
# Пользователю предлагается угадать заданное число.
# При каждой попытке, если число не равно заданному, програма сообщает больще или меньше введённое пользователем
# Если числа совпадают, то программа поздравляет с победой и сообщает количество попыток потребовавшихся для отгадывания

import random


# функция определяющая правильное окончание слова
def endword(value):
  if value < 11:
    if value == 1: return 'попытка'
    if value in [2, 3, 4]: return 'попытки'
    if value > 4: return 'попыток'
  if value > 10 and value < 21: return 'попыток'
  if value > 20:
    x = int(str(value)[-1])
    if x == 0: return 'попыток'
    if x == 1: return 'попытка'
    if x in [2, 3, 4]: return 'попытки'
    if x > 4: return 'попыток'
  return 'попыток'

guess = random.randint(1, 100)
userGuess = 0
cnt = 0

print('Добро пожаловать в игру "Угадай число"')
print('Компьютер загадывает число в диапазоне от 1 до 100.')
print('Ваша задача угадать его за наиментшее количество попыток.')
print('-' * 64)
print('Число выбрано, угадывайте!')

while userGuess != guess:
  userGuess = int(input('Ваш вариант?'))
  cnt += 1
  if userGuess > guess:
    print('Больше, немного уменьшите.')
  if userGuess < guess:
    print('Меньше, увеличьте.')
  if userGuess == guess:
    print('ПОЗДРАВЛЯЮ! Вы угадалии, число {} правильный вариант.'.format(guess))
    print('Для поиска числа вам потребовалось {} {}.'.format(cnt, endword(cnt)))
  if userGuess < 0:
    break

print()
print('-' * 64)
input('Нвжмите enter для выхода.')
