import ower


class ItemLoaned(object):
    """Object representing item loaned"""
    def __init__(self, ower, _item_id, _item_type, _item_value,
            _start_date, _end_date, _comment):

        self.the_ower = ower
        self.item_id = _item_id
        self.item_type = _item_type
        self.value = _item_value
        self.start_date = _start_date
        self.end_date = _end_date
        self.status = "Still Loaned"
        self.comment = _comment

    def change_status(self):
        """change the status of the object"""
        if self.status == "Still Loaned":
            self.status = "Given Back"
        else:
            self.status = "Still Loaned"

    def change_end_date(self, new_end_date):
        """# change the due date"""
        self.end_date = new_end_date




