# -*- coding: utf-8 -*-

__author__ = 'ufian'

from microbit import *
import radio
import random as r
import struct
from collections import namedtuple


radio.on()
radio.config(channel=43, queue=10, length=32, data_rate=radio.RATE_2MBIT)

INIT_STATE = 0
MASTER_STATE = 1
SLAVE_STATE = 2

state = INIT_STATE
start_time = None
identy = 0
identy_slaves = set()

params = dict()

MAX_IDENTY = 32000

Message = namedtuple('Message', ['receiver', 'sender', 'message'])
MESSAGE_FORMAT = 'II24s'

def message_send(m):
    radio.send_bytes(struct.pack(MESSAGE_FORMAT, *m))

def message_reseive():
    mstr = radio.receive_bytes()
    if mstr and len(mstr) == 32:
        return Message(*struct.unpack(MESSAGE_FORMAT, mstr))
    if mstr and len(mstr) != 32:
        print ('Error', mstr)

while True:
    if state == SLAVE_STATE:
        if start_time is None:
            start_time = running_time()
            identy = r.randint(1, MAX_IDENTY)
            display.scroll('S')
        
        message = message_reseive()
        if not message:
            continue
                
        if message and message.receiver == 0 and 'Master' not in params and message.message.startswith(b'Master'):
            params['Master'] = message.sender

            print('Wellcome', params['Master'])
            
            while identy == params['Master']:
                identy = r.randint(1, MAX_IDENTY)
            print('Slave', identy)
            message_send(Message(params['Master'], identy, 'Slave'))

        if 'Master' in params:
            if message.receiver == identy and message.sender == params['Master']:
                display.scroll(message.message[0:4])
        
    elif state == MASTER_STATE:
        if start_time is None:
            start_time = running_time()
            print("Start", start_time)
            identy = r.randint(1, MAX_IDENTY)
            display.scroll('M')
            
        if start_time + 10000 > running_time():
            message_send(Message(0, identy, "Master"))
        else:
            if 'end' not in params:
                print("End", running_time(), start_time)
                print('End Master')
                params['end'] = True
                
                for slave_id in identy_slaves:
                    message_send(Message(slave_id, identy, 'Ok'))
                    
        message = message_reseive()
        if message and message.receiver == identy:
            print("Receive")
            if message.message.startswith(b'Slave'):
                if message.sender not in identy_slaves:
                    identy_slaves.add(message.sender)
                    message_send(Message(message.sender, identy, 'Wait {0}'.format(message.sender)))
                    print('Wait', message.sender)
                else:
                    message_send(Message(message.sender, identy, 'Bad {0}'.format(message.sender)))
                    identy_slaves.remove(message.sender)
                    print('Bad', message.sender)
                
    else:
        display.scroll('W')
        if button_a.was_pressed():
            state = MASTER_STATE
        elif button_b.was_pressed():
            state = SLAVE_STATE