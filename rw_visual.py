import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
	# Построение случайного блуждания и нанесение точен на диаграмму.
	rw = RandomWalk(5000)
	rw.fill_walk()

	# Назначение размера области просмотра.
	plt.figure(dpi=128, figsize=(10, 6))

	point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
				# edgecolor='none', s=1)

	plt.plot(rw.x_values, rw.y_values, linewidth=1)

	# Выделение первой и последней точек.
	plt.scatter(0, 0, c='green', edgecolor='none', s=75)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
				s=75)

	# Удаление осей.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	# plt.savefig('molecular_motion.png', bbox_inches='tight')

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break