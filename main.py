from instagrapi import Client
import requests
import datetime
from dateutil.relativedelta import relativedelta

# instagram comfig
username = "manho"
password = "12345678"


# get current bio from instagram
def getBio():
    response = requests.get(f"https://instagram.com/{username}/channel/?__a=1")

    userinfo = response.json()["graphql"]

    bio = userinfo["user"]["biography"]
    return bio

# edit bio
def editBio(bio, feels):
    # split the bio to array form
    bio = bio.split()
    
    # define a variable to store the status string
    status = bio[5]

    status = list(status)
    
    # remove the first element of the status array
    status.pop(0)

    # add the new status to the status array by feels

    if feels == "y":
        # put green state if happy
        status.append("🟢")
        
        status = "".join(status)
        return status

    elif feels == "n":
        # ask again is your feelings bad
        # if yes, add 🔴 to the status array
        # if no, add 🟠 to the status array 

        askAgain = str(input("Is your feelings bad? (y/n) "))

        if askAgain == "y":
            status.append("🔴")

        elif askAgain == "n":
            status.append("🟠")

        status = "".join(status)
        return status


# asking todays feelings
feeling = str(input("What is your feeling today? (y/n) "))

# for debuging testing
testBio = """Status from 1/4 - 7/4 
🟢🟢🟢🟠🔴🟢🟢
[Updates by bot in Thu 7 April 21:12 ]
c^2 = a^2 + b^2
"""

status = editBio(testBio, feeling)
day1 = datetime.datetime.today() - datetime.timedelta(days=7) 
day1 = day1.strftime("%d/%m")
day7 = datetime.datetime.today().strftime("%d/%m")
now = datetime.datetime.today().strftime("%a %d %b %Y %H:%M")


BIO = """Status from {day1} - {day7}
{status}
[Updates by bot in {now}]
"""





#initial the ig client
ig = Client()
ig.login(username, password)
ig.account_edit(biography=f"{BIO.format(day1=day1, day7=day7, status=status , now=now)}")



# for debugging
print(editBio(getBio(), feeling))