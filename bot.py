from address_book_class import AddressBook
from dater_class import Dater
from record_class import Record


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'Give me actual name please.'
        except IndexError:
            return 'Give me name please.'
    return inner        

def parse_input(command):
    cmd,*args = command.split()
    cmd=cmd.strip()
    return cmd,args

@input_error
def add_contact(args,book:AddressBook):
    name,phone=args
    record=book.find(name)
    if record:
        record.add_phone(phone)
        return('contact updated')
    record=Record(name)
    record.add_phone(phone)
    book.add_record(record)
    # contacts[name]=phone
    return('contact added')

@input_error
def change_contact(args,book:AddressBook):
    name,phone=args
    record=book.find(name)
    record.add_phone(phone)
    # contacts[name]=phone
    return('contact changed')

@input_error
def show_phone(name,book:AddressBook):
    record=book.find(name)
    return(str(record))

@input_error
def add_birthday(args, book:AddressBook):
    name,birthday=args
    record=book.find(name)
    record.add_birthday(birthday)
    return('birthday added')


@input_error
def show_birthday(name, book:AddressBook):
    record=book.find(name)
    return record.show_birthday()

@input_error
def birthdays(book:AddressBook):
    return book.get_upcoming_birthdays()

def show_all(book:AddressBook):
    return str(book)

def main():
    book=AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        command,args=parse_input(command)

        match(command):
            case('close'):
                print("Good bye!")
                break  
            case('exit'):
                print("Good bye!")
                break 

            case('hello'):
                print("How can I help you?")

            case('add'):
                print(add_contact(args,book))

            case('change'):
                print(change_contact(args,book))

            case('phone'):
                print(show_phone(args,book))

            case('all'):
                print(show_all(book))

            case('add-birthday'):
                print(add_birthday(args,book))

            case('show-birthday'):
                print(show_birthday(args,book))

            case('birthdays'):
                print(birthdays(book))

            case(_):
                print("Invalid command.")


if __name__ == "__main__":
    main()