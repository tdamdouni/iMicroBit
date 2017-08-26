#!python2
# coding: utf-8
import cb
import time
import sys

class MyCentralManagerDelegate (object):
    def __init__(self):
        self.peripheral = None
        self.ledtext = None
        self.connected = False

    def did_discover_peripheral(self, p):
        print '+++ Discovered peripheral: %s (%s)' % (p.name, p.uuid)
        if p.name and 'BBC micro:bit [vutet]' in p.name and not self.peripheral:
            # Keep a reference to the peripheral, so it doesn't get garbage-collected:
            self.peripheral = p
            cb.connect_peripheral(self.peripheral)

    def did_connect_peripheral(self, p):
        print '*** Connected: %s' % p.name
        print 'Discovering services...'
        p.discover_services()

    def did_fail_to_connect_peripheral(self, p, error):
        print 'Failed to connect'

    def did_disconnect_peripheral(self, p, error):
        print 'Disconnected, error: %s' % (error,)
        self.peripheral = None
        self.ledtext = None
        self.connected = False

    def did_discover_services(self, p, error):
        for s in p.services:
            print '+++ Discovered services: %s' % (s.uuid)
            if 'E95DD91D-251D-470A-A062-FA1922DFA9A8' in s.uuid:
                print '+++ LED Service'
                p.discover_characteristics(s)

    def did_discover_characteristics(self, s, error):
        if 'E95DD91D-251D-470A-A062-FA1922DFA9A8' in s.uuid:
            for c in s.characteristics:
                if 'E95D93EE-251D-470A-A062-FA1922DFA9A8' in c.uuid:
                    self.ledtext = c
                    self.connected = True

    def disp_ledtext(self, text):
        if self.ledtext:
          self.peripheral.write_characteristic_value(self.ledtext, text, True)

delegate = MyCentralManagerDelegate()
print 'Scanning for peripherals...'
cb.set_central_delegate(delegate)
cb.scan_for_peripherals()

while not delegate.connected:
	pass

while delegate.connected:
   s = raw_input('text? ')
   if s == '':
      print 'Disconnect everything'
      cb.reset()
      break
   delegate.disp_ledtext(s)

sys.exit()

# Keep the connection alive until the 'Stop' button is pressed:
try:
    while True: pass
except KeyboardInterrupt:
    # Disconnect everything:
    cb.reset()
    
