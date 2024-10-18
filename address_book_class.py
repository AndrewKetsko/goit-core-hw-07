from collections import UserDict
from datetime import date
from record_class import Record
from dater_class import Dater

class AddressBook(UserDict):

    def __str__(self):
        list=''
        for record in self.data.values():
            list+=f'{record.name}: {[record.value for record in record.phones]}\n'
        return list
    
    def add_record(self,record:Record)->None:
        self.data[record.name.value]=record

    def find(self,name:str)->Record|None:
       return self.data.get(name)
    
    def delete(self,name:str)->None|str:
        try:
            del self.data[name]
        except KeyError:
            return f'Name {name} is not in your phonebook'
        
    # def find_next_weekday(self, start_date, weekday):
    #     days_ahead = weekday - start_date.weekday()
    #     if days_ahead <= 0:
    #         days_ahead += 7
    #     return start_date + timedelta(days=days_ahead)
        
    # def adjust_for_weekend(self, birthday):
    #     if birthday.weekday() >= 5:
    #         return self.find_next_weekday(birthday, 0)
    #     return birthday

    # def date_to_string(self, date):
    #     return date.strftime("%Y.%m.%d")
        
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for user in self.data.values:
            birthday_this_year = user["birthday"].replace(year=today.year)

            if birthday_this_year<today:
                birthday_this_year=birthday_this_year.replace(year=today.year+1)
            
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year=Dater.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = Dater.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": user["name"], "birthday": congratulation_date_str})

        return upcoming_birthdays
