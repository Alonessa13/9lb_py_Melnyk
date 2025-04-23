# Функції для розрахунків
def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years
def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor
def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    if speed_of_light_fraction >= 1:
        return "Помилка: швидкість не може бути більшою або рівною швидкості світла."
    return time_seconds / (1 - speed_of_light_fraction)
# Приклад виклику функцій і виведення результатів
# Космічна відстань
speed = 0.7
time_years = 5
cosmic_distance = calculate_cosmic_distance(speed, time_years)
print(f"Приблизна космічна відстань становить: {cosmic_distance} світлових років.")
# Спрощена гравітація
mass1 = 500
mass2 = 600
gravity = calculate_simplified_gravity(mass1, mass2)
print(f"Спрощене гравітаційне притягання становить: {gravity} одиниць сили.")
# Наближення сповільнення часу
speed_of_light_fraction = 0.9
time_seconds = 100
slowed_time = calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds)
print(f"Наближене сповільнення часу становить: {slowed_time} секунд.")
