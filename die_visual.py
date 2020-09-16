import pygal
from die import Die 

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = [die.roll() for i in range(1000)]

# Анализ результатов.
frequencies = [results.count(i) for i in range(1, die.num_sides + 1)]

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(i) for i in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')