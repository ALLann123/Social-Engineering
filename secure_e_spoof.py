from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import sys

print("******Starting******")
# SMTP Configuration
smtp_server = ""  # Brevo SMTP server
port = 000   # Brevo SMTP port
username = ""  # Your Brevo login email
password = ""  # Your Brevo SMTP password
print("Checking SMTP configs")

if port!=587 and smtp_server == "":
    print("[-]Error!!Set the SMTP configurations inthe code")
    sys.exit()

else:
    print("[+]Confirmed!!")


# Sender and Recipient Information
from_addr = input("Enter from Email address>> ")  # Sender's email
to_addr = input("Enter the target email address>> ")  # Recipient's email
sender_name = input("Enter Senders Name>> ")  # Sender's name
reply_to_addr = input("Enter Reply email>> ")  # Address to redirect replies to

# Email Content
print("----------------------------------------")
print("[+]Compose Email")
subject = input("Enter the Subject of email>> ")
html_template_file = input("Enter the HTML Template to Use>> ")

def send_html_email():
    try:
        # Read the HTML template
        with open(html_template_file, 'r') as file:
            message = file.read()

        # Replace placeholders in the HTML template
        message = message.replace("{{FirstName}}", "Allan")

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = f"{sender_name} <{from_addr}>"
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg['Reply-To'] = reply_to_addr  # Redirect replies to this email
        msg.attach(MIMEText(message, "html"))

        # Send the email
        with SMTP(smtp_server, port) as smtp:
            smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(from_addr, to_addr, msg.as_string())
            print("HTML email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Main Function
if __name__ == "__main__":
    send_html_email()
