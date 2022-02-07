import shutil
import smtplib
path = '/'
host_name = 'host_name'

# in Bytes
total, used, free = shutil.disk_usage(path)

total_GB = round(total / (2**30), 1)
used_GB = round(used / (2**30), 1)
free_GB = round(free / (2**30), 1)

quotient = round(used/total*100, 1)

print(f'Used: {used_GB} GB, Total: {total_GB} GB, Quotient: {quotient} % ')

if quotient >= 90:

    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    to = ['']
    subject = f'{host_name}: The disc is full!'
    body = f'{host_name}:\nThe disc is full for {quotient} %.\n{used_GB} GB of {total_GB} GB is used.'

    email_text = f'From: {sent_from}\nTo: {", ".join(to)}\nSubject: {subject}\n\n{body}'

    print(email_text)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print('Email sent successfully!')
    except Exception as ex:
        print('Something went wrong….',ex)

