from datetime import datetime
from field_class import Field

class Birthday(Field):
    def __init__(self,value):
        try:
            self.value = datetime.strptime(value,'%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return f'{self.value.strftime('%d.%m.%Y')}'
