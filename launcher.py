#!/usr/bin/python

# Owee
# Udacity final project
# this file is represents the controller of the app

import dashboard



# menu user input choice
choice = 0

# keep the app in a loop untill the user decides to quit
while int(choice) < 6:
	# prompt the user some kind of "UI" menu
	menu = """
	| ************************* Welcome to Owee ************************** |
	                                                                      
				What would you like to do?

	1. Add an owee
	2. Delete an owee
	3. Display Dashboard
	4. Change the status (your object was given back)
	5. Send a reminder message to the person owing you
	6. Quit
	> """

	# check for input validation from choices input
	try:
		# declare choice as input
		choice = int(raw_input(menu))
		if (choice == 1):
			# add a row to the dashboard
			print """ 

			Fill the form, enter 'none' if you don't want to fill an anwser

			 """
			print("1- Add an owee\n") 
			dashboard.add_line("owees.txt")
			print("\n...0wee successfully added\n")

		elif (choice == 2):
			# delete a row from the dashboard
			option = raw_input("Do you really want to delete the owee? There is no going back [y/n]: ")
			# this bool indicates that the id does not exist
			print("\n2- Delete an owee\n") 
			is_not_there = True
			if (option == "y"):
				# loop until the id entered exist
				while is_not_there:
					if dashboard.delete_line("owees.txt"):
						print("\n...Owee deleted successfully\n")
						is_not_there = False

					else:
						print("Eter a valid ID, type 'q' to quit")

			elif (option == "n"):
				print("\n...Operation canceled\n")

			else:
				print("Please type y for yes or n for no")	
			#break;		 

		elif (choice == 3):
			# display all owees in a webpage form
			owees = dashboard.file_to_list("owees.txt")
			dashboard.open_dashboard_page(owees)
			print("\n...Owee displayed successfully\n")

		elif (choice == 4):
			# change the status of an owee
			is_not_there = True
			# loop until the id entered exist
			while is_not_there:
				print("\n4- Change status\n") 
				if dashboard.change_status("owees.txt"):
					print("\n...Owee status updaated successfully\n")
					is_not_there = False

				else:
					print("Eter a valid ID, type 'q' to quit")

		elif (choice == 5):
			# send a message 

			print("message sent")
			#dashboard.send_message()

		elif (choice == 6):
			# display a message before quitting the app
			print("Bye... untill next time")	
		else:
			# if choice is not valid prompt this error message
			print("\nSorry but the choice has to be either 1, 2, 3, 4, 5 or 6\n")
			choice = 0

	except:
		print ("\nPlease enter a number as input\n")						
