age = int(input())
x = 220
max_puls = x - age
optimal_low_zone = int(max_puls / 100 * 60)
optimal_high_zone = int(max_puls / 100 * 70)

print(f'Максимальный пульс для Вас состаляет {max_puls} единицы')
print(f'Точка максимальной эффектиности в границе от {optimal_low_zone} до {optimal_high_zone} единиц')
