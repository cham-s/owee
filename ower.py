#! /usr/bin/python
# Udacity final Project
# Thi class is part of a app called owee

import time
from time import gmtime

# define ower 

class Owee():
	"""This class define all the attribute of an ower the person we lend the stuff to"""
	def __init__(self, ower_name, ower_email, lended_stuff, end_date):
		self.name = ower_name
		self.email = ower_email
		self.stuff = lended_stuff
		self.start = time.strftime("%a, %d %b %Y", gmtime())
		self.end = end_date
		self.status = "Still Lended"

		# this method send an email to the ower to kindly remind him of the stuff he borrowed
	#def reminder():
		# TODO: implement this later

	def change_status(self):
		if self.status == "Still Landed":
			self.status = "Given back"
		

			

