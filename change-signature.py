#!/usr/bin/python

#
# Copyright 2018 Chris Cartland. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

import qotd
DATA = {'signature': qotd.qotd()}   # quote source up-to-you!

SCOPES = 'https://www.googleapis.com/auth/gmail.settings.basic'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
  creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
# this entire block optional if you only have one sender address
addresses = GMAIL.users().settings().sendAs().list(userId='me',
        fields='sendAs(isPrimary,sendAsEmail)').execute().get('sendAs')
for address in addresses:
  if address.get('isPrimary'):
    break
rsp = GMAIL.users().settings().sendAs().patch(userId='me',
        sendAsEmail=address['sendAsEmail'], body=DATA).execute()
print("Signature changed to '%s'" % rsp['signature'])

