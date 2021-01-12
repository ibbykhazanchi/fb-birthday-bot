from fb import fb_birthday
import googleapi
import accessories
import messages

# get list of birthdays
username = '******@****.com'
password = '******'
birthday_people = fb_birthday(username, password).getBirthdays()
print("today's friends with bdays are: ")
print(birthday_people)

# get list of contacts from google
contacts_book = googleapi.get_contacts()
print("my list of contacts are: ")
print(contacts_book)

# search for bday person in contacts
from_mail = '******@****.com'
password = '******'

for person in birthday_people:
    number = ''

    try:
        number = contacts_book[person]
    except Exception:
        for contact in contacts_book:
            if person.upper() in contact.upper():
                number = contacts_book[contact]
    
    if number:
        number = accessories.clean_number(number)
        print("friend found! :")
        print("{}, {}".format(person, number))
        messages.send_text(from_mail, password, number)
        print("birthday message sent to {}".format(person))



        




