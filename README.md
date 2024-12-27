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

    copy your SMTP Server value in these case "smtp-relay.brevo.com" is the value of smtp_server inthe program
    copy the port 587, use the port number 587 as the value of port 
    copy login, which is your email address. Use the email as the value of username inthe program
    copy SMTP Key, which is the value of the password in the program
After coping the above values replace them in our script secure_e_spoof.py

        kali> git clone https://github.com/ALLann123/Social-Engineering.git
        kali> nano secure_e_spoof.py

![Screenshot 2024-12-27 021702](https://github.com/user-attachments/assets/f973b6f1-922d-494b-9033-02a481e68d84)

Save the script ctrl+s and ctrl+x to exit

Run the script

        kali> python3  secure_e_spoof.py
You should give it the fields requested inthe user input like inthe screenshot below
![send_process](https://github.com/user-attachments/assets/0ad5a516-2247-46a2-abba-8a08e553923a)
Keep in mind we provide the HTML template we would like to be displayed on the email, mine is template.html which is a html file stored inthe same directory as the script. You can use any HTML file you want in your deception.
When you get the response HTML EMAIL successful the deception worked!!!

Now check the targets email address to confirm they have received the Email.
![delivered](https://github.com/user-attachments/assets/33f9d31a-f320-4882-b1cf-81727636c7d8)

The best part about brevo SMTP server is that we can track our transaction to see if the target opened the Email

Go back to the brevo web site and click on the left menu transactions followed by statistics below it 
![track](https://github.com/user-attachments/assets/770a6e43-90a3-41a6-a3f6-5a0264178398)

# HTML Templates
These are templates we can use in our email spoofing to make the fake emails look more realistic. We can find them for free by searching on google "email phishing templates".
Because using python we are reading from a file and this allows us to use email templates, which are written in HTML
We have plenty of them e.g on the site https://caniphish.com/free-phishing-test/phishing-email-templates
![Screenshot 2024-12-27 045425](https://github.com/user-attachments/assets/d5436134-383f-46b5-8367-7cc64d999bbe)

# DISCLAIMER
USE FOR EDUCATION PURPOSE

For the deception to work it relies heavily on how much OSINT carried on a specific target. 

How does a computer get drunk? It takes screenshots.


