import smtplib, ssl, pandas, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


port = 465  # For SSL


sender_email = "keathrowaway+receiver@gmail.com"
usersFile = "curvexUsers.csv"
link = "zamknijmor.de"


def sendemail(user,performance):
    password = input("Type your password and press enter: ")
    context = ssl.create_default_context() # Create a secure SSL context for security reasons
    receiver_email = users.iloc[user]["email"]
    currentUser = users.iloc[user]["user_name"]
    if performance == "great":
        message = ( 
            f"Subject: Hey {currentUser}!  Here is your monthly summary."
            f"\n"
            f"We are impressed with your resaults. "
            f"You are doing great!"
            f"Thank you for being with us!\n"
            f"Here is a link for your summary\n"
            f"{link}\n"
            f"Keep on going!\n"
            f"Curvex Team"
        )
    elif performance == "ok":
        message = ( 
            f"Subject: Hey {currentUser}!"
            f"Here is your monthly summary.\n"
            f"You are on a way to a great performance!\n"
            f"Thank you for being with us!\n"
            f"Here is a link for your summary\n"
            f"{link}\n"
            f"How about trying these programs to boost your performance:....!\n"
            f"Curvex Team"
        )    
    else:
        message = ( 
            f"Subject: Hey {currentUser}!"
            f"Here is your monthly summary.\n"
            f"We can see that you weren't doing the best lately\n"
            f"Here is a link for your summary\n"
            f"{link}\n"
            f"You can try these programs:....!\n"
            f"Curvex Team"
        )
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email Sent")
def loadUsers():
    global users
    users = pandas.read_csv (usersFile,index_col= 0)
    print(users)

def sendPushNotification(user):
    print("Hey " + users.iloc[user]["user_name"]+" come back to us!")

loadUsers()
clear()
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
            sendemail(choice,"great")
        elif users.iloc[choice]["performance"] == "poor":
            sendemail(choice,"poor")
        elif users.iloc[choice]["performance"] == "ok":
            sendemail(choice,"ok")