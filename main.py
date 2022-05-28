def calculate(value):
    number = int(value)
    _res = "Привет" if number > 7 else 'Введите другое число'
    return _res


def task1():
    while True:
        val = input("Введите 'х' что бы закончить или число: ")
        if 'x' in val:
            break
        else:
            number = int(val)
            print(f'Результат работы программы для введённого значения \'{number}\' - {calculate(number)}')


def task2():
    val = input('Введите имя ')
    print(enter_name(val))


def enter_name(name: str) -> str:
    name = name.capitalize()
    if name == 'Вячеслав':
        return f'Привет, {name}'
    return 'Нет такого имени'


def multiple_of_three_generator(some_list):
    return [num for num in some_list if num % 3 == 0]


def task3():
    vals = input("Введите числа через запятую: ")
    print(multiple_of_three_generator(list(map(lambda _: int(_), vals.split(',')))))


if __name__ == '__main__':
    while True:
        task = input("Введите номер задания (1, 2, 3, х - для выхода) ")
        if '1' in task:
            task1()
            continue
        if '2' in task:
            task2()
            continue
        if '3' in task:
            task3()
            continue
        break