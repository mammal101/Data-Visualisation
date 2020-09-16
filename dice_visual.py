import pygal
from die import Die 

# Создание двух кубиков D8.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() * die_2.roll() for i in range(50000)]

# Анализ результатов.
frequencies = [results.count(i) for i in range(1, die_1.num_sides * die_2.num_sides + 1)]

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(i) for i in range(1, 37)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')