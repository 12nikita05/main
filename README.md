# main
import pyautogui as auto
import keyboard as key
import time

def press():
    start = input('Кнопка старт: ')
    stop = input('Кнопка стоп: ')
    while True:
        if key.is_pressed(start):
            auto.tripleClick()
        if key.is_pressed(stop):
            print('Конец')
            break

def hold():
    times = []
    once = []
    moving = []
    for i in range(int(input('Число точек: '))):
        times.append(int(input('Число кликов: ')))
        once.append(int(input('Задержка: ')))
    print('Наводись')
    time.sleep(2)
    for i in range(len(once)):
        print(auto.position())
        moving.append(auto.position())
        time.sleep(once[i])
    while True:
        for i in range(len(once)):
            auto.moveTo(moving[i])
            for g in range(times[i]):
                auto.tripleClick()
                print(g)

while True:
    print('Зажим - 1', '\n', 'Задающийся порядок - 2', sep='')
    key_word = input('Выберите режим: ')
    match key_word.lower():
        case '1':
            press()
        case '2':
            hold()
    print('Нажмите "s" для выхода', '\n', 'Нажмите "r" для продолжения', sep='')
    while True:
        flag = True
        if key.is_pressed('s'):
            flag = False
            break
        if key.is_pressed('r'):
            break
    if not flag:
        print('Конец')
        break
