#! /usr/bin/python
# Udacity final Project
# Thi class is part of a app called owee

import time
from time import gmtime
import csv

# define ower 

#def __init__(self, csv_file): reader = csv.reader(csv_file); and then assign to self.name, self.address

class Owee():
	"""This class define all the attribute of an ower the person we lend the stuff to"""
	def __init__(self, array_of_value):
		self.name = array_of_value[0]
		self.email = array_of_value[1]
		self.type = array_of_value[2]
		self.value = array_of_value[3]
		self.start = array_of_value[4]
		self.end = array_of_value[5]
		self.status = array_of_value[6]
		self.comment = array_of_value[7]

		# this method send an email to the ower to kindly remind him of the stuff he borrowed
	#def reminder():
		# TODO: implement this later

	def change_status(self):
		if self.status == "Still Landed":
			self.status = "Given back"

	# this method return array of all the owee propreties	
	def generate_row(self):
		row = [self.name, self.email, self.type, self.value, self.start, 
		self.end, self.status, self.comment]
		return row 

		

			

