#Реализовать модуль, содержащий функцию, которая возводит первый аргумент в степень, равную второму аргументу. Все значения имеют тип int.
import module
while True:
    try:
        arg1 = int(input("Введите первый аргумент:"))
        break
    except ValueError:
        print("Попробуйте еще раз:")

while True:
    try:
        arg2 = int(input("Введите второй аргумент:"))
        break
    except ValueError:
        print("Попробуйте еще раз:")
while True:
    order = input("Выберите порядок (arg1**arg2 или arg2**arg1): ")
    if order in ['arg1**arg2', 'arg2**arg1']:
        break
    else:
        print("Неверное значение. Попробуйте еще раз.")

result = module.stepen(arg1, arg2, order)
print(result)
