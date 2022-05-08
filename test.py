

import smtplib, ssl, pandas, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


port = 465  # For SSL


sender_email = "keathrowaway+receiver@gmail.com"
usersFile = "curvexUsers.csv"
link = "zamknijmor.de"


def sendemail(user):
    password = input("Type your password and press enter: ")
    context = ssl.create_default_context() # Create a secure SSL context for security reasons
    receiver_email = users.iloc[user]["email"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Hey " + users.iloc[user]["user_name"] + "! Here is your monthly summary."
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Thank you for being with us!
    Here is a link for your summary
    """ + link + """ 
    We wish you many more great whatever
    Curvex Team
    """
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def loadUsers():
    global users
    users = pandas.read_csv (usersFile,index_col= 0)
    print(users)

def sendPushNotification(user):
    print("Hey " + users.iloc[user]["user_name"]+" come back to us!")

loadUsers()
#clear()
print("Curvex CRM mockup")
usersPrint = users.drop("email",axis = 1).rename(columns={'user_name':'Name'})
print(usersPrint.to_string())

choice = int(input("Choose an user:")) - 1
if users.iloc[choice]["subscription"] == "no":
    print("Sorry this user is not a Subscriber")
else:
    if users.iloc[choice]["activity"] == "no":
        sendPushNotification(choice)
    else:
        if users.iloc[choice]["performance"] == "great":
            sendemail(choice)
        elif users.iloc[choice]["performance"] == "poor":
            sendemail(choice)
        elif users.iloc[choice]["performance"] == "ok":
            sendemail(choice)
