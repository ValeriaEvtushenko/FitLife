# Проект FitLife - MVP версия 1.0

# была ошибка в тесте:
# "FAILED tests/test_main.py::test_6_result - AttributeError:
# 'NoneType' object has no attribute 'strip'"
# поэтому добавила sys по совету gpt
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')


WATER_PER_KG = 30
ML_PER_L = 1000


def calculate_bmi(weight, height):
    """Функция расчёта индекса массы тела"""
    # расчёт индекса массы тела
    bmi = weight / (height ** 2)
    # округление значения bmi для лучшей читаемости
    bmi_rounded = round(bmi, 1)
    return bmi_rounded


def calculate_water(weight):
    """Функция  расчёта нормы воды"""
    # расчёт нормы воды
    water_ml = weight * WATER_PER_KG
    # перевод water_ml в литры
    water_l = water_ml / ML_PER_L
    # округление значения water_l для лучшей читаемости
    water_l_rounded = round(water_l, 1)
    return water_l_rounded


# 1. Знакомство
print('\n' + '=' * 25 + ' FIT LIFE ' + '=' * 25 + '\n')
print('Спасибо за выбор нашего приложения! Давай познакомимся :)')

user_name = input('Введи своё имя: ')
user_age = int(input('Сколько тебе лет? '))

print(f'\nПриятно познакомиться, {user_name}!')

# 2. Сбор данных
print('Давай введем о тебе некоторые данные.')

user_weight = float(input('Введи свой вес в килограммах: '))
user_height = float(input('Введи свой рост в метрах (например, 1.75): '))

# 3. Расчеты
print('\nВысчитаем ИМТ и норму воды...')

bmi = calculate_bmi(user_weight, user_height)
water_needed = calculate_water(user_weight)

# 4. Вывод красивого результата
print('\n' + '-' * 60)
print(f'\nОтчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день')
print('\nРасчет окончен. Будьте здоровы!')
print('\n' + '-' * 60 + '\n')
