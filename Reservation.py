class Reservation:
	def __init__(self, name, time):
		self.time = time
		self.name = name

	def get_time(self):
		return self.time

	def get_name(self):
		return self.name

	def set_name(self, n):
		self.name = n

	def set_time(self, t):
		self.time = t
