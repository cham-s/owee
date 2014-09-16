#!/usr/bin/python

# Owee
# Udacity final project
# this file is where the owee will be added

import ower
import dashboard


# declare choice to select in the menu

# menu user input choice
choice = "0"

while int(choice) < 7 or len(choice) < 2:
	# prompt the user on his intention
	menu = """
	| ************************* Welcome to Owee ************************** |
	                                                                      
	What would you like to do?
	1- Add an owee
	2- Delete an owee
	3- Display owee
	4- Change the status (your object was given back)
	5- Send a reminder message to the person owing you
	6- Quit
	> """

	# check for input validation of choice
	if choice.isdigit():
		choice = str(raw_input(menu)).strip()
		try:
			if (choice == "1"):
				try:
					dashboard.add_line()
					print("0wee successfully added")
				except:
					print("Something went wrong")	

			elif (choice == "2"):
				option = ""
				while option > 1:
					option = raw_input("Do you really want to delete the owee? There is no going back [y/n]: ")
					if (option == "y"):
						dashboard.delete_line()
						print("Owee deleted")	
					elif (option == "n"):
						print("Opearation canceled")
					else:
						print("Please y as yes or n as no")	
					break;		 

			elif (choice == "3"):
				try:
					dashboard.display_dashboard()
					print("Owee displayed")
				except: 
					print("Something went wrong")	

			elif (choice == "4"):
				try:
					#dashboard.change_stattus()
					print("Owee status successfully changed")
				except:
					print("Something went wrong")	

			elif (choice == "5"):
				print("mail sent")
				#dashboard.send_mail()
			else:
				print("Sorry but the choice has to be either 1, 2 or 3")
		except:
			print("enter number")			

	else:
		print ("Please enter only one number as input")
