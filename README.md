# Social-Engineering
"Specifics help, but specifics don't change the way that everyone is vulnerable. It just changes the way that we access those vulnerabilities" Mobley, Mr.Robot

# Email Spoofing with Python
![spoof_python](https://github.com/user-attachments/assets/190607e8-0948-4b55-8ca6-11e59c5641c4)

# Secure Email Spoofing
The second tool uses SMTPS which is a secure version of SMTP protocol that does message exchanges over a TLS connection. The tool relies on a public SMTP server to be able to send the email. We will be using Brevo(formerly sendinblue) to perform our deception.
Sign up for a free account https://www.brevo.com/
![brevo](https://github.com/user-attachments/assets/dfe8f8d1-c79e-445e-bfae-c862cd8e4d1d)

Onthe left handmenu click Transaction, followed by settings.
You'll see a menu and click configuration that below it briefly describes SMTP configuration
![config brevo](https://github.com/user-attachments/assets/82421569-24ac-4bed-83b4-e9cd41f5a7a5)
On SMTP Relay click on get your SMTP key
Generate your key
You should see something similar to these to get started with the code
![api key brevo](https://github.com/user-attachments/assets/fce8126d-d110-4ce1-aa4d-5ee2c1c4ec3c)

    copy your SMTP Server value
    copy the port 587
    copy login, which is your email address
    copy SMTP Key
After coping the above values replace them in our script secure_e_spoof.py

        kali> git clone 
