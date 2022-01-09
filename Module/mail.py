import smtplib as s
obj=s.SMTP("smtp.gmail.com",587)
obj.ehlo()
obj.starttls()
obj.login("shreekrishna9099@gmail.com","shree Krishna")
obj.sendmail("shreekrishna9099@gmail.com","jpvasoya444@gmail.com","Hello Everyone its work")
print("send mail")
obj.quit()