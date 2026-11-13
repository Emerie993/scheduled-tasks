import datetime as dt 
import pandas
import random
import smtplib
##################### Extra Hard Starting Project ######################
my_mail = "dantheecreator@gmail.com"
my_password = "eyjhylpwifajfoah"
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.now()
today_turple = (today.month,today.day)

birthdays = {(row.month,row.day) : row for (index,row) in data.iterrows()}

for birthday,data in birthdays.items():
    if today_turple == (birthday):
        letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

        with open(f"letter_templates/{random.choice(letters)}") as picked_letter:
            letter = picked_letter.read()
            formated_letter = letter.replace("[NAME]",data["name"])

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=data["email"],
                msg=f"Subject:Happy birthday pedophile\n\n {formated_letter}"
            )




# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

