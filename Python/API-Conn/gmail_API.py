import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError 


#Email Message
email_body = f"""
Hello,

[Message]

Thanks,
.py"""


#Gmail API Credentials
SCOPES = [ "https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file(r'C:/Users//creds.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)


#Email Details
message = MIMEText(email_body)
message['to'] = 'btrent@email.com'
message['subject'] = 'Hello World!'


#Send Email
create_message =  {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

try:
    result = (service.users().messages().send(userId="me", body=create_message).execute())
    print(f"""
          Message Delivered!""")
except HTTPError as error:
    print(f'An error occured {error}')
    result = None    