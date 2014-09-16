#! /usr/bin/python
# Udacity final Project
# Thi class is part of a app called owee


# define ower 

#def __init__(self, csv_file): reader = csv.reader(csv_file); and then assign to self.name, self.address

class Ower():
	"""This class define all the attributes of the person borrowing the item"""
	def __init__(self, ower_first_name, ower_last_name, ower_email, ower_phone, ower_address):
		self.first_name = ower_first_name
		self.last_name =  ower_last_name
		self.email =  ower_email
		self.phone = ower_phone
		self.address =  ower_address

		# this method send an email to the ower to kindly remind him of the stuff he borrowed
	#def reminder():
		# TODO: implement this later


		

			

