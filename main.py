##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
from random import choice
import smtplib
import datetime as dt

MY_EMAIL = "joshtipon921@gmail.com"
PASSWORD = "lrxxuboggxswwmin"

today = dt.datetime.now()
today_month = today.month
today_day_of_month = today.day

data = pandas.read_csv("birthdays.csv")
# print(data)

for name, row in data.iterrows():
    if row.month == today_month and row.day == today_day_of_month:
        letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        chosen_letter = choice(letter_templates)

        with open(chosen_letter, "r") as letter:
            greeting = letter.readlines()

        greeting[0] = greeting[0].replace("[NAME]", str(row["name"]))
        message = ''.join(greeting)
        print(message)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=f"{row.email}",
                                msg=f"Subject:Happy Birthday!\n\n{message}")
