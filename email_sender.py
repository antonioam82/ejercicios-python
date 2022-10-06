from yagmail import SMTP

def Email_Sender(subject, body):
    mail = SMTP(user='username', password='password')
    mail.send("reciever@mail.com", subject = subject, contents = body)
    mail.close()
    print("Email Sent")
    
def Email_With_Attachment(subject, attachment):
    mail = SMTP(user='username', password='password')
    mail.send("reciever@mail.com", subject = subject, attachments = attachment)
    print("Email Sent")
    
# main
Email_Sender("Subject101", "Hello from Medium")
Email_With_Attachment("Subject102",  ["img1.png", "img2.png"])
