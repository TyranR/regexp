from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


with open('phonebook_raw.csv', encoding='utf-8', newline='') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def main():
  """
  Основная программа
  """
  new_contact_list = []
  for contact in contacts_list:
    #Задача 1 ----------
    lastname = re.split(" ",contact[0])
    firstname = re.split(" ",contact[1])
    surname = re.split(" ",contact[2])
    initials = lastname + firstname + surname
    new_elem = []
    new_elem.append(initials[0])
    new_elem.append(initials[1])
    new_elem.append(initials[2])
    # Задача 1 ----------
    new_elem.append(contact[3])
    new_elem.append(contact[4])
    number = phone(contact[5])
    new_elem.append(number)
    new_elem.append(contact[6])
    new_contact_list.append(new_elem)
  final_contact_list = union(new_contact_list)
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_contact_list)


def phone(number):
  """
  Задача 2
  привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер,
  формат будет такой: +7(999)999-99-99 доб.9999;
  """
  if number == "phone":
    return "phone"
  else:
    pattern = '\w'
    raw_digit = re.findall(pattern, number)
    # Переводим номер телефона из списка в строку
    digit = ""
    for each in raw_digit:
      summ = digit + str(each)
      digit = summ
    if len(digit) == 11:
      result = re.sub(r'(\d)(\d{3})(\d{3})(\d\d)(\d\d)', r'7(\2)\3-\4-\5', digit)
    else:
      result = re.sub(r'(\d)(\d{3})(\d{3})(\d\d)(\d\d)([а-я]+)(\d{4})', r'7(\2)\3-\4-\5 \6. \7', digit)
    return result


def union(many_contacts):
  """
  Объединяем все дублирующиеся записи о человеке в одну
  """
  for contact in many_contacts:
    lastname_target = contact[0]
    firstname_target = contact[1]
    for test_contact in many_contacts:
      lastname_sourse = test_contact[0]
      firstname_sourse = test_contact[1]
      if (lastname_target == lastname_sourse and firstname_target == firstname_sourse):
        if contact[2] == "": contact[2] = test_contact[2]
        if contact[3] == "": contact[3] = test_contact[3]
        if contact[4] == "": contact[4] = test_contact[4]
        if contact[5] == "": contact[5] = test_contact[5]
        if contact[6] == "": contact[6] = test_contact[6]
  without_copy = []
  for each in many_contacts:
    if each not in without_copy:
      without_copy.append(each)
  return without_copy


main()

