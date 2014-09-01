# the dashboard display all the owee transaction

import webbrowser
import os


# declare the dashboard header
main_page_head ='''
<head>
<meta charset="UTF-8">
<title>Twitter Bootstrap 3 Fixed Layout Example</title>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
<style type="text/css">
    body{
    	padding-top: 70px;
    }
</style>
</head>
'''


# declare the dashboard main content
main_page_content = '''
<!DOCTYPE html>
<html lang="en">

</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col-md-2">nothing</div>
			<div class="col-md-10">
				<table class="table table-striped">
		<thead>
			<tr>
				<th>Name</th>
				<th>Stuff</th>
				<th>Start Date</th>
				<th>Due Date</th>
				<th>Status</th>
				<th>Actions</th>
			</tr>
			<tr>
		</thead>
		<tbody>
			{ower_rows}
		</tbody>	
	</table>
			</div>
		</div>
	</div>
	<script src="js/myscript.js">
</body>
</html>
'''

# ower row template
ower_row = '''
<tr>
	<td>{ower_name}</td>
	<td>{lended_stuff}</td>
	<td>{start_date}</td>
	<td>{end_date}</td>
	<td>{status}</td>
	<td><button type="button" class="btn btn-primary">Primary</button><span> </span><button type="button" class="btn btn-success">Success</button></td>
</tr>
'''
# create a single row fill with dynamic content
def create_ower_row_content(owers):
	# create rows content
	content = ''
	for ower in owers:
		# append with previous entry
		content += ower_row.format(
		ower_name=ower.name,
		lended_stuff=ower.stuff,
		start_date=ower.start,	
		end_date=ower.end,
		status=ower.status
		) 
	return content	

# open a webbrowser with all owees	

def open_dashbord_page(owers):
	# create or overwrite the ouput file
	output_file = open('dashboard.html', 'w')

	# replace the placeholder for the owee with dynamic content
	rendered_content = main_page_content.format(ower_rows=create_ower_row_content(owers))

	#output the file
	output_file.write(main_page_head + rendered_content)
	output_file.close()

	#open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2) # open in a new tab if possible

#













