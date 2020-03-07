from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re



with open("phonebook_raw.csv", encoding='utf-8', newline='') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)



with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)