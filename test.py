def func(x):
    return 5 / (3*x - x*x - 3)


x_start = float(input("Введите начальную точку отрезка x: "))
h = float(input("Введите шаг h (>0): "))

while h <= 0:
    print("Шаг h должен быть положительным!")
    h = float(input("Введите шаг h (>0): "))

x_end = x_start + h

current_x = x_start
min_x = current_x
min_y = func(current_x)

while current_x <= x_end:
    y = func(current_x)
    if y < min_y:
        min_y = y
        min_x = current_x
    current_x += h

print(f"Локальный минимум функции на отрезке [{x_start}, {x_end}]:")
print(f"x = {round(min_x, 3)}, y = {round(min_y, 3)}")
# print(f"Сделал")
