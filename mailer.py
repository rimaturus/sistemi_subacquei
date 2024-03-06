import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'your_smtp_server'
smtp_port = 587  # Change if necessary
sender_email = 'edo.ca1999@gmail.com'
sender_password = ''
subject = 'Your subject here'
message_body = 'Your message here'

# List of recipients
recipients = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# Create message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject

# Attach message body
msg.attach(MIMEText(message_body, 'plain'))

# Connect to SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    # Login to sender email
    server.login(sender_email, sender_password)
    # Send email
    text = msg.as_string()
    server.sendmail(sender_email, recipients, text)
    print('Email sent successfully.')
except Exception as e:
    print(f'Error: {e}')
finally:
    # Quit SMTP server
    server.quit()
