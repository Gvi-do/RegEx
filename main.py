import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


count = 0
for list in contacts_list:
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


for contact in contacts_list[1:]:
    text = re.split('\s+', (f'{contact[0]} {contact[1]} {contact[2]}'))
    contact[0],contact[1],contact[2] = text[0],text[1],text[2]



pprint(contacts_list)



