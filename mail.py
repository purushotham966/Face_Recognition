import smtplib
try:
    
                
                
                
    mail=smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.login("tekuripurushotham@gmail.com","Sreenu@966")
    mail.sendmail("tekuripurushotham@gmail.com","tekuripurushotham@gmail.com","unknown person detected")
    mail.close()
    print("Mail sent")
    
    
except:
                
    print("failed")
