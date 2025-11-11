import math


def circle_area(r):
    # возвращает площадь круга.
    # Параметры:
    # r: радиус круга
    # Возвращаемое значение:
    # число, являющееся произведением числа пи на r в квадрате.
    if r <= 0:
        return "wrong input"
    return math.pi * r * r

def circle_perimeter(r):
    # возвращает периметр круга.
    # Параметры:
    # r: радиус круга
    # Возвращаемое значение:
    # число, являющееся произведением числа пи на r и 2.
    if r <= 0:
        return "wrong input"
    return 2 * math.pi * r

