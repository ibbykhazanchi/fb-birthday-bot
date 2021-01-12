from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

def get_contacts():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    results = service.people().connections().list(resourceName='people/me', personFields='names,emailAddresses,phoneNumbers', pageSize=1000).execute()
    connections = results.get('connections', [])

    contactbook = {}
    for person in connections:
        names = person.get('names', [])
        phone_numbers = person.get('phoneNumbers', [])
        if names and phone_numbers:
            name = names[0].get('displayName')
            phone_no = phone_numbers[0].get('value')
            if name and phone_no:
                contactbook[name] = phone_no
    
    return contactbook

