import Reservation

reservations = []

class Restaurant: 
	# def __init__(self):
	# 	# self.reservations = [] # number

	def add_reservation(self, res):
		print(' i am in add reservation')
		availability = True
		print(len(reservations))

		for i in reservations:
			if res == i:
				print('here')
				print i
				#suggest alternate time
				availability = False

		if availability == True:
			reservations.append(res)
			print len(reservations)
		#sort list
		print('end add')
		return availability
	
	def alternate_reservation(self, res):
		available_before = True
		available_after = True

		des_time = res
		for i in reservations:
			print('i am printing des_time')
			print(des_time)
			#check one hour before and after for available
			if i == (des_time + 1):
				available_after = False
			elif i == (des_time - 1):
				available_before = False
				#make i.get_time the time for teh reservation
				#add reservation to teh list
		avail_times = []
		if available_before == True:
			avail_times.append(des_time - 1)
		if available_after == True:
			avail_times.append(des_time + 1)

		return avail_times







