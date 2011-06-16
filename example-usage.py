#!/usr/bin/env python

import sipgate
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
    sg = sipgate.api(MY_SIPGATE_USERNAME, MY_SIPGATE_PASSWORD)
    ### Query the phonebook
    phonebook = sg.PhonebookListGet()
    all_entry_ids = [entry['EntryID'] for entry in phonebook['PhonebookList']]
    all_phonebook_entries = sg.PhonebookEntryGet({'EntryIDList': all_entry_ids})
    # Print all entries (they are vCards)
    print json.dumps(all_phonebook_entries, indent=2)
    ### Query the history for your SIP-ID:
    history = sg.HistoryGetByDate()
    print json.dumps(history, indent=2)
### Error handling:
except sipgate.SipgateAPIFault, e:
    stderr.write( 'A problem occured: "%s" (Fault code: %d).\n' %(e.faultString, e.faultCode) )
except sipgate.SipgateAPISocketError, e:
    stderr.write( 'A low level network communication error occured: %s.\n' % e)
except sipgate.SipgateAPIException, e:
    stderr.write( 'Some other problem accured while communicating with the Sipgate API: %s' % e )
except Exception as e:
    stderr.write( 'A unpredicted problem of the type %s occured: %s' % (type(e), e) )
