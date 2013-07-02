#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sipgate import api, SipgateAPIException, helpers
import json
from sys import stderr

### You may set your Sipgate credentials here in this file or in settings.py (to be created by you):
MY_SIPGATE_USERNAME='Fill_in_your_Sipgate_username_here'
MY_SIPGATE_PASSWORD='Fill_in_your_Sipgate_password_here'
try:
    from settings import *
except:
    pass

try:
    s = api(MY_SIPGATE_USERNAME, MY_SIPGATE_PASSWORD, 'example script')

    ### Query the phonebook
    phonebook = s.PhonebookListGet()
    all_entry_ids = [entry['EntryID'] for entry in phonebook['PhonebookList']]
    all_phonebook_entries = s.PhonebookEntryGet({'EntryIDList': all_entry_ids})
    ### Print all entries (they are vCards)
    print json.dumps(all_phonebook_entries, indent=2)
    ### New API version (different URL, not for basic / plus accounts): print json.dumps( s.EventSummaryGet(), indent=2) 

    ### Query the history for your SIP-ID:
    history = s.HistoryGetByDate()
    print json.dumps(history, indent=2)

    ## Let's find out your default Sipgate Uri:
    default_uri = 'sip:NULL@sipgate.net'
    for own_uri in s.OwnUriListGet()['OwnUriList']:
        if own_uri['DefaultUri']: default_uri = own_uri['SipUri']

### now some functions that are commented out for the moment: adjust the variables
### recipient_number, text, number_to_dial, recipient_number, pdf_file for the respective sections:

    #  ### Send an SMS (commented out for now in order not to send an sms all the time)
    #  recipient_number, text = '49123456789', "Hello, I'm testing the Sipgate XML-RPC API."
    #  ## SessionInitiate may return the following server status codes in case of errors: 501, 502, 506, 520, 525
    #  sms = s.SessionInitiate({'LocalUri': default_uri, 'RemoteUri': 'sip:%s@sipgate.de' % recipient_number, 'TOS': 'text', 'Content': text })
    #  print json.dumps(sms, indent=2)

    # ### Initiate a call (click2dial):
    # number_to_dial = '49123456789'
    # print json.dumps( s.SessionInitiate({'RemoteUri': 'sip:%s@sipgate.de' % number_to_dial, 'LocalUri': default_uri, 'TOS': 'voice'}) )

    #  ### Send a fax (commented out for now in order not to send an sms all the time)
    #  import base64
    #  recipient_number, pdf_file = '49123456789', 'sample_file.pdf'
    #  fax_base64 = base64.b64encode(open(pdf_file, 'rb').read())
    #  print json.dumps(s.SessionInitiate({ 'RemoteUri': 'sip:%s@sipgate.de' % recipient_number, 'TOS': 'fax', 'Content': fax_base64 }))

    ### get server data (SIP server, stun server, etc.)
    serverdata = s.ServerdataGet()
    print json.dumps(serverdata, indent=2)

    ### get your SIP addresses
    uris = s.OwnUriListGet()
    print json.dumps(uris, indent=2)

    ### get your SIP connection credentials:
    print json.dumps(s.UserdataSipGet({'LocalUriList':[sipuri['SipUri'] for sipuri in uris['OwnUriList'] ]}), indent=2)

    ### get your first and last name + gender:
    print json.dumps(s.UserdataGreetingGet(), indent=2)

### Error handling:
except SipgateAPIException, e:
    helpers.ShowSipgateErrors(e)
    exit(2)
except Exception as e:
    stderr.write( 'A unpredicted problem of the type %s occured: %s' % (type(e), e) )
    exit(3)

