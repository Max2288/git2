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
        elif command == 'fibonacci':
            number = int(input('Введите номер элемента последовательности: '))
            print(fib(number))
        elif command == 'first_order':
            mat = [[int(number) for number in input('Строка матрицы ').split()]
                   for doings in range(1)]
            print(opredelitel_first_order(mat))
        elif command == 'sec_order':
            mat = [[int(number) for number in input('Строка матрицы ').split()]
                   for doings in range(2)]
            print(opredelitel_second_order(mat))
        if command == 'third_order':
            mat = [[int(number) for number in input('Строка матрицы ').split()]
                   for doings in range(3)]
            print(opredelitel_third_order(mat))

