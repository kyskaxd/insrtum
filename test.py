def func(x):
    return 5 / (3*x - x*x - 3)

x_start = float(input("Введите начальную точку: "))
x_end = float(input("Введите конечную точку: "))
h = float(input("Введите шаг h (>0): "))

if h <= 0:
    print("Шаг h должен быть положительным")
    exit()

current_x = x_start

min_x = x_start
min_y = func(x_start)


while current_x <= x_end:
    current_y = func(current_x)    
    if current_y  < min_y:
        min_y = current_y 
        min_x = current_x
    current_x += h

print(f"x = {round(min_x, 3)}, y = {round(min_y, 3)}")

