"""Illustrate ours programms."""
from functions import opredelitel_first_order
from functions import opredelitel_second_order
from functions import opredelitel_third_order
from functions import fib


if __name__ == '__main__':
    print('Список команд: \nfibonacci - запускает фибоначи \nfirst_order - считает определитель\
первого порядка \nsec_order - считает определитель второго порядка \nthird_order - \
считает определитель третьего порядка \noff - завершает программу')
    while True:
        command = input('Введите команду: ')
        if command == 'off':
            print('Программа завершена!')
            break
        
