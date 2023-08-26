# import smtplib
#
# my_email = "cloakingpie2038@gmail.com"
# password = "napiaojyufdyizwm"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # TLS = Transport Layer Security: Allows messages to be encrypted and be secured
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="uishauvei@yahoo.com",
#                         msg="Subject:Hello\n\nWassup nurd!"
#                         )
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)

# ------------------------- SUNDAY QUOTES ------------------------- #
import smtplib
import datetime as dt
from random import choice

my_email = "cloakingpie2038@gmail.com"
password = "napiaojyufdyizwm"

now = dt.datetime.now()
weekday_to_check = 6  # Sunday (6)
now_weekday = now.weekday()

if now_weekday == weekday_to_check:
    print(f"{now_weekday} == {weekday_to_check}")
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()

    quote = choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # TLS = Transport Layer Security: Allows messages to be encrypted and be secured
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="uishauvei@yahoo.com",
                            msg=f"Subject:Quote of The Day\n\n{quote}"
                            )

