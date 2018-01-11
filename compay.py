import pickle, os

def total():
		with open('value.dat', 'rb') as file:
			data = pickle.load(file)
			print('Вода:')
			print('Предыдущие показания:',data[0])
			a=int(input('Введите новое значение:'))
			r = a-data[0]
			w = r*40.98

			print('Газ:')
			print('Предыдущие показания:',data[2])
			c=int(input("Введите новое значение: "))
			r2=c-data[2]
			g=r2*5.88652

			print('Электроэнергия:')
			print('Предыдущие показания:',data[1])
			b =int(input('Введите новое значение: '))
			r1 = b-data[1]
			print('Израсходовано света:\n {:.2f} Квт'.format(r1))
			if r1 <= 250:
				e = r1 *3.72
				print('Сумма за свет:\n {:.2f} руб.'.format(e))
			else:
				e=250*3.72+(r1-250)*5.19
				print('Сумма за свет:\n {:.2f} руб.'.format(e))

			garbage=data[3]
			total=w+g+e+garbage

			print('Израсходовано воды:\n {:.2f} м3'.format(r))
			print('Сумма за воду:\n {:.2f} руб.'.format(w))
			print('Израсходовано газа:\n {:.2f} м3'.format(r2))
			print('Сумма за газ:\n {:.2f} руб.'.format(g))
			print('Сумма за мусор:\n',garbage, 'руб')
			print('Всего:\n {:.2f} руб'.format(total))

		data = [0,1,2,3]
		data[0] = a
		data[1] = b
		data[2] = c
		data[3] = 360
		with open('value.dat', 'wb') as file:
			pickle.dump(data, file)

		with open('Total.txt', 'w') as file:
			file.write('Израсходовано воды:\n {:.2f} м3\n'.format(r))
			file.write('Сумма за воду:\n {:.2f} руб.\n'.format(w))
			file.write('Израсходовано света:\n {:.2f} Квт\n'.format(r1))
			file.write('Сумма за свет:\n {:.2f} руб.\n'.format(e))
			file.write('Израсходовано газа:\n {:.2f} дм3\n'.format(r2))
			file.write('Сумма за газ:\n {:.2f} руб.\n'.format(g))
			file.write('Сумма за мусор:\n {:.2f} руб.\n'.format(garbage))
			file.write('Всего:\n {:.2f} руб'.format(total))

if not os.path.isfile('value.dat'):

	data = [0,1,2,3]
	data[0] = int(input('Введите показания воды на конец месяца: '))
	data[1] = int(input('Введите показания света на конец месяца: '))
	data[2] = int(input('Введите показания газа на конец месяца:'))
	data[3] = 360

	with open('value.dat', 'wb') as file:
		pickle.dump(data, file)

	total()

else:
	total()

		
