#!/usr/bin/env python

import time
from stomp_sender import send_message_via_stomp, StompConnectionException, \
                         StompMessageException

brokers = [('1.2.3.4', 61616), ('4.3.2.1', 61616)]
headers = {'destination': '/queue/events',
           'timestamp': int(time.time() * 1000), 'eventtype': 'Fluxo'}
params = {'propriedade1': 'valor1', 'propriedade2': 'valor2'}
try:
    send_message_via_stomp(brokers, headers, params)
except (StompConnectionException, StompMessageException):
    print 'Error connecting or sending message to STOMP sender'
else:
    print 'Message sent!'

