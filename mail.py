#**if you access google account on other applications ,you should turn less secure app "ON" in your accounts
#just search "less secure apps" on google to get direct link.


import smtplib
try:
                
    mail=smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.login(" mail_id","write_password")
    mail.sendmail("from mail_id","receiver mail_id","unknown person detected")
    mail.close()
    print("Mail sent")
    
    
except:
                
    print("failed")
