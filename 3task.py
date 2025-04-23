# Отримання числових даних з обробкою помилок
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Помилка! Ви повинні ввести число. Спробуйте ще раз.")
# Приклад використання функції для запиту даних
print("Введення даних для розрахунків космічних таємниць!")
speed = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
time_years = get_float_input("Введіть час у роках: ")
mass1 = get_float_input("Введіть масу першого об'єкта: ")
mass2 = get_float_input("Введіть масу другого об'єкта: ")
