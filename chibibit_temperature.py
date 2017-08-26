#!python2
# coding: utf-8
import cb

def s8(value):
	return -(value & 0b10000000) | (value & 0b01111111)

class MyCentralManagerDelegate (object):
    def __init__(self):
        self.peripheral = None
        self.ledtext = None
        self.toggle = False

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

    def did_discover_services(self, p, error):
        for s in p.services:
            print '+++ Discovered services: %s' % (s.uuid)
            if 'E95DD91D-251D-470A-A062-FA1922DFA9A8' in s.uuid:
                print '+++ LED Service'
                p.discover_characteristics(s)
            elif 'E95D6100-251D-470A-A062-FA1922DFA9A8' in s.uuid:
                print('+++ temperature Service found')
                p.discover_characteristics(s)

    def did_discover_characteristics(self, s, error):
        if 'E95DD91D-251D-470A-A062-FA1922DFA9A8' in s.uuid:
            for c in s.characteristics:
                if 'E95D93EE-251D-470A-A062-FA1922DFA9A8' in c.uuid:
                    self.ledtext = c
        elif 'E95D6100-251D-470A-A062-FA1922DFA9A8' in s.uuid:
            for c in s.characteristics:
                if 'E95D9250-251D-470A-A062-FA1922DFA9A8' in c.uuid:
                     print('Enabling notifications for temperature Service...')
                     self.peripheral.set_notify_value(c, True)
                elif 'E95D1B25-251D-470A-A062-FA1922DFA9A8' in c.uuid:
                     print('Set Temperature Period...')
                     #Set Temperature Period 5000ms
                     self.peripheral.write_characteristic_value(c, '\x88\x13', True)

    def did_write_value(self, c, error):
    	pass

    def did_update_value(self, c, error):
        if 'E95D9250-251D-470A-A062-FA1922DFA9A8' == c.uuid:
            print('Temperature value: %s (0x%s)' % (s8(ord(c.value)), c.value.encode('hex')))
            self.peripheral.write_characteristic_value(self.ledtext, str(s8(ord(c.value))), True)

delegate = MyCentralManagerDelegate()
print 'Scanning for peripherals...'
cb.set_central_delegate(delegate)
cb.scan_for_peripherals()

# Keep the connection alive until the 'Stop' button is pressed:
try:
    while True: pass
except KeyboardInterrupt:
    # Disconnect everything:
    cb.reset()
