def mail(count):

# PRG1: ライブラリ設定
import smtplib
from email.mime.text import MIMEText
 
count=0
if count==1:
    # PRG2: メール情報の設定
    from_email ='junaaajdtpaw@gmail.com' 
    to_email = 'kmatsushita1012@icloud.com' 
    cc_mail = ''
    mail_title = 'test'
    message = 'カンニングが検出されました'
    '''
    '''
    
    # PRG3: MIMEオブジェクトでメールを作成
    msg = MIMEText(message, 'plain')
    msg['Subject'] = mail_title
    msg['To'] = to_email
    msg['From'] = from_email
    msg['cc'] = cc_mail
    
    # PRG4: サーバを指定してメールを送信する
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_password = 'ygyknvknuwmmpzyc'
    
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(from_email, smtp_password)
    server.send_message(msg)
    server.quit()