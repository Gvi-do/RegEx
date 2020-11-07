import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def phone_format(contacts):
    count = 0
    for list in contacts:
      if 'доб.' in list[5]:
        pattern1 = re.compile(r'[+7|8]+[ (]+(\d+)[ )-]+(\d+)[ -](\d+)[ -](\d+)[ |(]+(доб\.)[ ](\d+)[)]?')
        list[5] = pattern1.sub(r'+7(\1)\2-\3-\4 \5\6', list[5])
        count +=1

      elif count == 2:
        pattern2 = re.compile(r'[+7|8]+(\d{3})(\d{3})(\d{2})(\d{2})')
        list[5] = pattern2.sub(r'+7(\1)\2-\3-\4', list[5])
        count += 1
      elif count == 3:
        pattern3 = re.compile(r'[+7|8]+ (\d{3})-(\d{3})-(\d{2})(\d{2})')
        list[5] = pattern3.sub(r'+7(\1)\2-\3-\4', list[5])
        count +=1
      else:
        pattern = re.compile(r'[+7|8]+[ (]+(\d+)[ )-]+(\d+)[ -](\d+)[ -](\d+)')
        list[5] = pattern.sub(r'+7(\1)\2-\3-\4', list[5])
        count += 1

def name_format(contacts):
    for contact in contacts[1:]:
        text = re.split('\s+', (f'{contact[0]} {contact[1]} {contact[2]}'))
        contact[0],contact[1],contact[2] = text[0],text[1],text[2]

def removing_duplicates(contacts):
    new_contacts_list = []

    for idx,contact in enumerate(contacts):
        result = contact
        if idx + 1 < len(contacts):
            for contact2 in contacts[idx + 1:]:
                if contact[0] == contact2[0]:
                    result = [max(p) for p in zip(result, contact2)]
                    contacts.remove(contact2)
            new_contacts_list.append(result)
        else:
            new_contacts_list.append(result)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_contacts_list)

phone_format(contacts_list)
name_format(contacts_list)
removing_duplicates(contacts_list)


