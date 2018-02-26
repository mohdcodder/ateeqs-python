import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("rehman.mohammed00010@gmail.com", "Welcome@786")

msg = "Hello!"

server.sendmail("rehman.mohammed00010@gmail.com", "rehman.mohammed00010@gmail.com", msg)

server.quit()
