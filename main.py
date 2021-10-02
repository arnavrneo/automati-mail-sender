# CAUTION: IN ORDER TO TEST THIS CODE, FIRST CHANGE THE DATE AND MONTH IN "birthdays.csv" TO THE CUR DATE

import smtplib
import pandas
import datetime as dt
import random

now = dt.datetime.now()
month = now.month
day = now.day
today_tuple = (month, day)

my_email = ""  # write email here
my_pass = ""   # write pass here

birthday = pandas.read_csv("birthdays.csv")
dict_data = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday.iterrows()}  # IMP!!

letter_1 = open("letter_templates/letter_1.txt")
letter_2 = open("letter_templates/letter_2.txt")
letter_3 = open("letter_templates/letter_3.txt")
letters_list = [letter_1, letter_2, letter_3]


def letter_maker_and_sender():
    birthday_person = dict_data[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    print(letter_file)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f'Subject:Happy Birthday\n\n {contents}')
    connection.close()


def verify():
    if today_tuple in dict_data:
        letter_maker_and_sender()


verify()

