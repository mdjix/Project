from datetime import datetime
import time


def func(n):
    list1 = []
    for i in range(n):
        list1.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
    return list1


result = func(int(input('Введите число: ')))
print(result)

