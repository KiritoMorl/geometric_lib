# Библиотека для нахождения площадей и периметров
## Ниже описаны формулы, функции и история коммитов

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


# Functions

## Area
```
Для круга находит площадь, необходимые параметры:
r - радиус круга.
Пример вызова:
- area(3)  вернет 9π
- area(2)  вернет 4π

Для квадрата находит площадь, необходимые параметры:
а - сторона квадрата.
Пример вызова:
- area(3)  вернет 9
- area(2)  вернет 4

Для треугольника находит площадь, необходимые параметры:
а - сторона треугольника,
h - высота треугольника.
Пример вызова:
- area(3, 4)  вернет 6
- area(2, 1)  вернет 1 
```

## Perimeter
```
Для круга находит периметр, необходимые параметры: r - радиус круга.
Пример вызова:
- perimeter(3)  вернет 6π
- perimeter(1)  вернет 2π

Для квадрата находит периметр, необходимые параметры:
а - сторона квадрата.
Пример вызова:
- perimeter(3)  вернет 12
- perimeter(2)  вернет 8

Для треугольника находит периметр, необходимые параметры:
а - длина 1 стороны треугольника,
b - длина 2 стороны треугольника,
c - длина гипотенузы.
Пример вызова:
- perimeter(3, 4, 5)  вернет 12
- perimeter(2, 1, 5)  вернет 8 
```
# Commits history

1.  * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
2.  * 438b89a L-05: Add user agreement
3.  * 6adb962 L-03: Docs added
4.  | * 3049431 (origin/feature) L-04: Add rectangle.py
5.  | | * b5b0fae (origin/develop) L-04: Update docs for calculate.py
6.  | | * d76db2a L-04: Add calculate.py
7.  | | * 51c40eb L-04: Doc updated for triangle
8.  | | * d080c78 L-04: Triangle added
9.  | |/  
10. | * d078c8d (HEAD -> main, origin/main, origin/HEAD) L-03: Docs added
    |/  
11. * 8ba9aeb L-03: Circle and square added
