# the dashboard display all the owee transaction

import webbrowser
import ower
import time
from time import gmtime
import csv
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

            <div class="row placeholders">
              <div class="col-xs-6 col-sm-3 placeholder">
                <img data-src="holder.js/200x200/auto/sky" src="img/simple.png" class="img-responsive" alt="Generic placeholder thumbnail">
                <h4>Label</h4>
                <span class="text-muted">Something else</span>
              </div>
              <div class="col-xs-6 col-sm-3 placeholder">
                <img data-src="holder.js/200x200/auto/vine" src="img/6charts.png" class="img-responsive" alt="Generic placeholder thumbnail">
                <h4>Label</h4>
                <span class="text-muted">Something else</span>
              </div>
              <div class="col-xs-6 col-sm-3 placeholder">
                <img data-src="holder.js/200x200/auto/sky" src="img/simple.png" class="img-responsive" alt="Generic placeholder thumbnail">
                <h4>Label</h4>
                <span class="text-muted">Something else</span>
              </div>
              <div class="col-xs-6 col-sm-3 placeholder">
                <img data-src="holder.js/200x200/auto/vine" src="img/6charts.png" class="img-responsive" alt="Generic placeholder thumbnail">
                <h4>Label</h4>
                <span class="text-muted">Something else</span>
              </div>
            </div>

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

# add csv line
def add_line():
	# generate number with uuid only take the 5 numbers from the begining
	owee_id = str(uuid.uuid4().fields[-1])[:5]
	name = str(raw_input("Enter name: ")).strip()
	email = str(raw_input("Enter email: ")).strip()
	object_type = str(raw_input("Enter type: ")).strip()
	value = str(raw_input("Enter value: ")).strip()
	start_date = time.strftime(" %d %b %Y", gmtime())
	end_date = str(raw_input("Enter a due date: ")).strip()
	owee_status = "Still lended"
	comment = str(raw_input("Enter a note regarding the transaction: ")).strip()

	row = [owee_id, name, email, object_type, value, start_date, end_date, owee_status, comment]
	csv_line = ", ".join(row)

	f = open("owees.csv", "a")
	f.write(csv_line + '\n')

	f.close()


# create a single row fill with dynamic content
def create_ower_row_content(owees):
	# create rows content
	content = ''
	for owee in owees:
		# append with previous entry
		content += owee_row.format(
		owee_id=owee.o_id,	
		owee_name=owee.name,
		object_type=owee.type,
		value=owee.value,
		start_date=owee.start,	
		end_date=owee.end,
		status=owee.status,
		note=owee.comment
		) 
	return content	

# open a webbrowser with all owees	

def open_dashbord_page(owees):
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




# return csv fil rows as array
def csv_to_array(csv_filename):
	rows = []

	with open(csv_filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
	   		rows.append(row)
	return rows   		

# add a row and open the webpage with new 
def add_owee():
	add_line()
	owees = []
	rows = csv_to_array('owees.csv')

	for row in rows:
		owees.append(ower.Owee(row))

	# after	 adding a row, display the dashboard
	open_dashbord_page(owees)


	

















