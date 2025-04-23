# Функція для розрахунку космічної відстані
def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    distance = speed_of_light_fraction * time_years
    return distance
# Функція для розрахунку спрощеної гравітації
def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    gravity = mass1 * mass2 * cosmic_factor
    return gravity
# Функція для розрахунку наближення сповільнення часу
def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    if speed_of_light_fraction >= 1:
        return "Швидкість не може бути більшою або рівною швидкості світла"
    time_dilated = time_seconds / (1 - speed_of_light_fraction)
    return time_dilated
# Приклади використання функцій
# Розрахунок космічної відстані
distance = calculate_cosmic_distance(0.5, 10)
print("Космічна відстань:", distance, "світлових років")
# Розрахунок спрощеної гравітації
gravity = calculate_simplified_gravity(1000, 2000)
print("Спрощена гравітація:", gravity)
# Розрахунок наближення сповільнення часу
time_dilated = calculate_time_dilation_approximation(0.8, 100)
print("Сповільнення часу:", time_dilated, "секунд")
