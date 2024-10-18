from datetime import datetime

class Birthday:
    def __init__(self,value):
        try:
            self.birthday = datetime.strptime(value,'%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
