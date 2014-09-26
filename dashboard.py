# the dashboard display all the owee transaction

import webbrowser
import item
import ower 
import time
from time import gmtime
import pickle
import os
import uuid



# declare the dashboard header
main_page_head ='''
<head>
<meta charset="UTF-8">
<title>Owee - keep track of them</title>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
<style type="text/css">
    body{
    	padding-top: 70px;
    }
</style>
<link rel="stylesheet" type="text/css" href="css/dashboard.css">
</head>
'''


# declare the dashboard main content
main_page_content = '''
<!DOCTYPE html>
<html lang="en">

<body>
  
  <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Owee</a>
        </div>
        <div class="navbar-collapse collapse">
          
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="col-md-12 col-lg-12">
            <h1 class="page-header">Overview</h1>

     
            <h2 class="sub-header">Owees</h2>
            <div class="table-responsive">
              <table class="table table-striped">
                <thead>
                  <tr>
                  	<th>Owee ID</th>
                    <th>Name</th>
                    <th>Object Type</th>
                    <th>Value</th>
                    <th>Start date</th>
                    <th>Due date</th>
                    <th>Status</th>
                    <th>Note</th>
                  </tr>
                  </thead>
                  <tbody>   

                  {owee_rows}
                  
                </tbody>  
              </table>

            </div>
          </div>
        </div>
    </div>

  </body>
</html>
'''

# ower row template
owee_row = '''
				<tr>
					<td>{owee_id}</td>
					<td>{owee_name}</td>
					<td>{object_type}</td>
					<td>${value}</td>
					<td>{start_date}</td>
					<td>{end_date}</td>
					<td>{status}</td>
					<td>{note}</td>
				<tr>
				'''

# return a list of object
def file_to_list(filename):
	# open file to read and load objects
	if os.path.getsize(os.getcwd() + "/" + filename) > 0:
		f = open(filename, "rb")
		try:
			object_list = pickle.load(f)
			return object_list
		except EOFError:
			return None
		f.close()	
	else:
		object_list = []
		return object_list			
	

# open a file to write and modifies it	
def modify_file(list_of_object, filename):
	# open and write objects to file
	f = open(filename, "wb")
	pickle.dump(list_of_object, f)
	f.close()	


# add an object to this list
def add_line(filename):
	first_name = str(raw_input("Enter first name: ")).strip()
	last_name = str(raw_input("Enter last name: ")).strip()
	email = str(raw_input("Enter email: ")).strip()
	address = str(raw_input("Enter adddess: ")).strip()
	phone = str(raw_input("Enter a phone number: ")).strip()
	# generate a 5 digit unique id
	owee_id = str(uuid.uuid4().fields[-1])[:5]
	item_type = str(raw_input("Enter type: ")).strip()
	item_value = str(raw_input("Enter value: ")).strip()
	start_date = time.strftime(" %d %b %Y", gmtime())
	end_date = str(raw_input("Enter a due date: ")).strip()
	owee_status = "Still lended"
	comment = str(raw_input("Enter a note regarding the transaction: ")).strip()

	the_ower = ower.Ower(first_name, last_name, email, phone, address)


	item_loaned = item.ItemLoaned(the_ower, owee_id, item_type, item_value, start_date,
                end_date, owee_status, comment)

	owees = file_to_list(filename)
	owees.append(item_loaned)

	modify_file(owees, filename)



	

def change_state(filename, state):
	search_id = ""
	owees = file_to_list(filename)
	# iterator
	i = 0
	id_is_not_there = True
	# check if id exits and proceed accordingly
	while id_is_not_there:
		search_id = str(raw_input("Enter the owee ID: ")).strip()
		for owee in owees:
			if search_id == owee.item_id:
				# option to delete a row
				if state == "delete":
					del(owees[i])
				# option to change owee status
				elif state == "status":
					owee.change_status()
				# option to change the end date	
				elif state == "date":
					new_end_date = raw_input("\nEnter new date (format: dd month year): ")
					owee.change_end_date(new_end_date)
				else:
					print ("Invalid state")
				id_is_not_there = False	
			i += 1			
		if id_is_not_there:
			print("Please enter a valid ID or 'q' to quit. ")	
		else:
			print("\n...Operation succeded\n")
					
		if search_id == "q":
				print("\n...Operation canceled.\n")
				break;

	modify_file(owees, filename)


# create a single row fill with dynamic content
def create_ower_row_content(owees):
	# create rows content
	content = ''
	for owee in owees:
		# append with previous entry
		content += owee_row.format(
		owee_id=owee.item_id,	
		owee_name=owee.the_ower.first_name,
		object_type=owee.item_type,
		value=owee.value,	
		start_date=owee.start_date,	
		end_date=owee.end_date,
		status=owee.status,
		note=owee.comment
		) 
	return content	

# open a webbrowser with all owees	

def open_dashboard_page(owees):
	# create or overwrite the ouput file
	output_file = open('dashboard.html', 'w')

	# replace the placeholder for the owee with dynamic content
	rendered_content = main_page_content.format(owee_rows=create_ower_row_content(owees))

	#output the file
	output_file.write(main_page_head + rendered_content)
	output_file.close()

	#open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2) # open in a new tab if possible




  		


	



	

















