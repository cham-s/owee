#!/usr/bin/python

# Owee
# Udacity final project
# this file is represents the controller of the app

import dashboard

# menu user input choice
choice = 0

# keep the app in a loop until the user decides to quit
while int(choice) < 7:
    # prompt the user some kind of "UI" menu
    menu = '''
    | ************************* Welcome to Owee ************************** |

                What would you like to do?

    1. Add an owee
    2. Delete an owee
    3. Display Dashboard
    4. Change the status (reverse the current status Still Loaned/Given Back)
    5. Send a reminder message to the person owing you
    6. Modify due date
    7. Quit
    > '''

    # check for input validation from choices input
    try:
        # declare choice as input
        choice = int(raw_input(menu))
        if choice == 1:
            # add a row to the dashboard
            print """

            Fill the form, enter 'none' if you don't want to fill an anwser

             """
            print("1- Add an owee.\n")
            # the .ol file is a custom made extension for object list or owee list file
            dashboard.add_line("owees.ol")
            print("\n...0wee successfully added.\n")

        elif choice == 2:
            # delete a row from the dashboard
            option = raw_input("Do you really want to delete the owee? There is no going back [y/n]: ")
            print("\n2- Delete an owee.\n")

            # agree to delete owee
            while option != "y" and option != "n":
                option = raw_input("Please type y for yes or n for no: ")
            if option == "y":
                dashboard.change_state("owees.ol", "delete")

            # refuse to delete owee
            elif option == "n":
                print("\n...Operation canceled.\n")

        elif choice == 3:
            # display all owees in a webpage form
            owees = dashboard.file_to_list("owees.ol")
            dashboard.open_dashboard_page(owees)

        elif choice == 4:
            # change the status of an owee
            dashboard.change_state("owees.ol", "status")

        elif choice == 5:
            # send a message
            dashboard.change_state("owees.ol", "reminder")

            print("TO DO: implement this")
            #dashboard.send_message()
        elif choice == 6:
            # change the due date
            dashboard.change_state("owees.ol", "date")


        elif choice == 7:
            # display a message before quitting the app
            print("\nBye... until next time\n")
        else:
            # if choice is not valid prompt this error message
            print("\nSorry but the choice has to be either 1, 2, 3, 4, 5, 6 or 7\n")
            choice = 0

    except Exception, e:
        print str(e)
        print ("\nPlease enter a number as input\n")
