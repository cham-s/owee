import ower

class ItemLoaned(object):
	"""Object representing item loaned"""
	def __init__(self, ower_first_name, ower_last_name, ower_email, ower_phone, ower_address, 
	_item_id, _item_type, _item_value, _start_date, _end_date, status, _comment):

		self.the_ower = ower.Ower(ower_first_name, ower_last_name, ower_email, ower_phone, ower_address)
		self.item_id = _item_id
		self.item_type = _item_type
		self.value = _item_value
		self.start_date = _start_date
		self.end_date = _end_date
		self.status = "Still Loaned"
		self.comment = _comment

		# change the status
		def change_status(self):
			if self.status == "Still Loaned":
				self.status = "Given back"	
