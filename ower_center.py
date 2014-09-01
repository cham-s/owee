#!/usr/bin/python

# Owee
# Udacity final prjoect
# this file is where the owee will be added

import ower
import dashboard


# declare choice to select in the menu

# prompt the user on his intention
menu = """
What would you like to do?
1- Add an owee
2- Delete an owee
3- Display owee
> """

# menu user input choice
choice = "0"

# check for input validation of choice
if choice.isdigit():
	while choice > 3 or choice < 0:
		choice = str(raw_input(menu)).strip()
		if (choice == "1"):
			#dashboard.addOwee()
			print("owee added")
			break;
		elif (choice == "2"):
			print("owee deleted")
			#dashboard.deleteOwee()
			break;
		elif (choice == "3"):
			print("owee displayed")
			#dashboard.displayOwee()
			break;
		else:
			print("Sorry but the choice has to be either 1, 2 or 3")			

else:
	print ("Please enter only one number as input")