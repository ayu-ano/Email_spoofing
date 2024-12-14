import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

your_email = "your_email or hacked _ email id "
your_password = "your_ app password "

if not your_email or not your_password:
    logging.error("SMTP credentials are not set correctly. Please set the environment variables.")
    exit(1)

# Correct Gmail SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(spoofed_from_name, to_email, subject, body):
    try:
        msg = MIMEMultipart()
        
        # Format the spoofed_from with name and email
        spoofed_from = f"{spoofed_from_name} "
        
        msg['From'] = spoofed_from
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade connection to a secure encrypted connection
            server.login(your_email, your_password)
            server.sendmail(your_email, to_email, msg.as_string())

        logging.info(f"Email successfully sent to {to_email}")

    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    spoofed_from_name = "Support Team"  # Set your desired name here
    to_email = 'recipent@gmail.com'
    subject = 'Urgent Action Required: Important Email'
    body = '''Dear User,

    This is an important message that requires your immediate attention. Please respond as soon as possible.

    Regards,
    The Support Team'''

    send_email(spoofed_from_name, to_email, subject, body)

if __name__ == '__main__':
    main()

