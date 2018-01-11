import pickle, os
# This function calculate my communal payments
def total():
		with open('value.dat', 'rb') as file: 	#open value file 
			data = pickle.load(file)
			print('Water:')
			print('Last value:',data[0]) 		#Load water value
			a=int(input('Enter new value:'))
			r = a-data[0]						#Count the amount of water expended
			w = r*40.98							#Calculate the amount of payment

			print('Gas')
			print('Last value:',data[2])		#Load gas value	
			c=int(input('Enter new value:'))	
			r2=c-data[2]						#Count the amount of gas expended
			g=r2*5.88652						#Calculate the amount of payment

			print('Electric power:')
			print('Last value:',data[1])		#Load electric power value
			b =int(input('Enter new value:'))
			r1 = b-data[1]						#Count the amount of electric power expended
			print('Consumed electricity:\n {:.2f} kw'.format(r1))
			if r1 <= 250:						#Сompare the expenditure with the social norm per family
				e = r1 *3.72					#Calculate the amount of payment
				print('Amount of electric power expended:\n {:.2f} rub.'.format(e))
			else:
				e=250*3.72+(r1-250)*5.19		#Calculate the amount of payment
				print('Amount of electric power expended:\n {:.2f} rub.'.format(e))

			garbage=data[3]						#Load garbage value	
			total=w+g+e+garbage					#total amount calculation

			print('Spent water:\n {:.2f} cbm'.format(r))
			print('Amount for water expended:\n {:.2f} rub.'.format(w))
			print('Spent gas:\n {:.2f} cdm'.format(r2))
			print('Amount for gas expended:\n {:.2f} rub.'.format(g))
			print('Fee for garbage disposal:\n',garbage, 'rub')
			print('Total:\n {:.2f} rub'.format(total))
		#rewrite all value
		data = [0,1,2,3]
		data[0] = a
		data[1] = b
		data[2] = c
		data[3] = 360
		with open('value.dat', 'wb') as file:
			pickle.dump(data, file)
		#Write result to file
		with open('Total.txt', 'w') as file:
			file.write('Spent water:\n {:.2f} м3\n'.format(r))
			file.write('Amount for water expended:\n {:.2f} руб.\n'.format(w))
			file.write('Consumed electricity:\n {:.2f} Квт\n'.format(r1))
			file.write('Amount of electric power expended:\n {:.2f} руб.\n'.format(e))
			file.write('Spent gas:\n {:.2f} дм3\n'.format(r2))
			file.write('Amount for gas expended:\n {:.2f} руб.\n'.format(g))
			file.write('Fee for garbage disposal:\n {:.2f} руб.\n'.format(garbage))
			file.write('Total:\n {:.2f} руб'.format(total))

if not os.path.isfile('value.dat'):
#Write value
	data = [0,1,2,3]
	data[0] = int(input('Enter last water value: '))
	data[1] = int(input('Enter last electric power value: '))
	data[2] = int(input('Enter last gas value: '))
	data[3] = 360

	with open('value.dat', 'wb') as file:
		pickle.dump(data, file)

	total()

else:
	total()

		
