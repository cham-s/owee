#!/usr/bin/python

# Owee
# Udacity final project
# this file is where the owee will be added

import dashboard


# declare choice to select in the menu

# menu user input choice
choice = 0

while int(choice) < 6:
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
	try:
		choice = int(raw_input(menu))
		if (choice == 1):
			try:
				dashboard.add_line("owees.txt")
				print("0wee successfully added")
			except:
				print("Something went wrong")	

		elif (choice == 2):
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

		elif (choice == 3):
			try:
				owees = dashboard.file_to_list("owees.txt")
				dashboard.open_dashboard_page(owees)
				print("Owee displayed successfully")
			except: 
				print("Something went wrong")	

		elif (choice == 4):
			try:
				#dashboard.change_stattus()
				print("Owee status successfully changed")
			except:
				print("Something went wrong")	

		elif (choice == 5):
			print("mail sent")
			#dashboard.send_mail()
		elif (choice == 6):
			print("Bye... till next time")	
		else:
			print("Sorry but the choice has to be either 1, 2, 3, 4, 5, 6")
	except:
		print ("Please enter a number as input")						
