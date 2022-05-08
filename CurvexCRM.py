import smtplib, ssl, pandas, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

##########
#Funtion that clears
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


port = 465  # Required For SSL

# strings used to establish data required for proper code execution
sender_email = "keathrowaway+receiver@gmail.com"
usersFile = "curvexUsers.csv"

#Funciton that sends an email based on users performance
def sendemail(user,performance):
    password = input("Type your password and press enter: ")
    context = ssl.create_default_context() # Create a secure SSL context for security reasons
    receiver_email = users.iloc[user]["email"]
    currentUser = users.iloc[user]["user_name"]

    msg = MIMEMultipart()
    
    msg['From'] = sender_email
    msg['To'] = receiver_email

    if performance == "great":
            msg['Subject'] =   f"Subject: Hey {currentUser}!  Here is your monthly summary."
            message = MIMEText(
            f"Hello {currentUser}.\nWe hope you are doing great\n"
            f"We are impressed with your results.\n"
            f"You are doing great!\n"
            f"Have a look at the summary in attachment.\n"
            f"Keep on going!\n\n"
            f"Thank you for being with us!\n"
            f"Curvex Team"
            )
            with open("yourSummary.png", 'rb') as f:
                img_data = f.read()
            msg.attach(message)
            image = MIMEImage(img_data, name=os.path.basename("yourSummary.png"))
            msg.attach(image)


    elif performance == "ok":
            msg['Subject'] =   f"Subject: Hey {currentUser}!  Here is your monthly summary."
            message = MIMEText(
            f"Hello {currentUser}.\nWe hope you are doing great\n"
            f"Here is your monthly summary.\n"
            f"You are on a way to a great performance!\n"
            f"Check out your activity summary in attachment\n"
            f"You can also try these programs to boost your performance:....!\n\n"
            f"Thank you for being with us!\n"
            f"Curvex Team"
            )
            with open("Summary.png", 'rb') as f:
                img_data = f.read()
            msg.attach(message)
            image = MIMEImage(img_data, name=os.path.basename("Summary.png"))
            msg.attach(image)
    else:
            msg['Subject'] =   f"Subject: Hey {currentUser}!  Here is your monthly summary."
            message = MIMEText(
            f"Hello {currentUser}.\nWe hope you are doing great\n"
            f"We can see that your sessions weren't going the best lately\n"
            f"Have a look at your monthly summary in attachments\n"
            f"Try these meditation programs and see how good they work for you!\n\n"
            f"Thank you for being with us!\n"
            f"Curvex Team"
            )
            with open("chart.png", 'rb') as f:
                img_data = f.read()
            msg.attach(message)
            image = MIMEImage(img_data, name=os.path.basename("chart.png"))
            msg.attach(image)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email Sent")

########
#Funtion used to read csv file and translate it into dataframe
def loadUsers():
    global users
    users = pandas.read_csv (usersFile,index_col= 0)
    print(users)

########
#Funtion Used to send not active user push notification
def sendPushNotification(user):
    print("Hey " + users.iloc[user]["user_name"]+" come back to us!")

# Main Program logics
loadUsers()
clear()
print("Curvex CRM mockup")
usersPrint = users.drop("email",axis = 1).rename(columns={'user_name':'Name'})
print(usersPrint.to_string())

choice = int(input("Choose an user:")) - 1
#If statement goes through precreated logic (as seen on whiteboard model)
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