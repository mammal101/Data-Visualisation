import pygal
from die import Die 

# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() + die_2.roll() for i in range(50000)]

# Анализ результатов.
frequencies = [results.count(i) for i in range(2, die_1.num_sides + die_2.num_sides)]

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [str(i) for i in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dif_dice_visual.svg')