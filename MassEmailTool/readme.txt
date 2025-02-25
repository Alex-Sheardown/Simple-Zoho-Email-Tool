-Zohomail  bulk email application readme-

-This application uses the Zohomail service to send emails to addresses listed in a CSV file.

-The user's credentials are required to send through the SMTP protocol.

-The provided text and CSV files are for the message to be sent and the recipient emails.

-Four fields are required: The subject of the email, the sender's email address (your Zoho account email), the recipient's email address, and a password.

-This password is an app password that is generated in the application specific passwords section from the following URL:

-->https://accounts.zoho.com/home#security/app_password

-Please keep in mind this is treated like an API Key. IT IS SHOWN ONCE AND CANNOT BE RECOVERED. So please ensure it is written down or copied to a secure location.



-The application has simple error handling though if an email is sent to a non existent address or it is blocked, Zohomail will send an email to your account detailing the error. I am not sure if I can perform error handling for those cases as this occurs after the email is sent.

-For now, the message you want to send must be typed into a simple text file, and I want to be able to add more fields for the CSV file potentially.

-The file names being read are static right now as well, but they're easily changeable within the code.

-I may or may not implement more features, it is pretty barebones but it works.



-It should be as easy as writing your message in the emailbody text file and providing emails and names for the recipients within the  emailspreadsheets CSV file, then clicking run.
-The formatting of the message should be preserved, given an example that it was modified in something like Open Office or Word.

-I'd like to have it eventually run as a command line app for more ease of use.

-Thanks for reading!