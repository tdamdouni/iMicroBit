#include "MicroBitCustomConfig.h"
#include "MicroBit.h"
#include "ble/DiscoveredCharacteristic.h"
#include "ble/DiscoveredService.h"

#if YOTTA_CFG_MICROBIT_S130 != 1
#error This code *only* works with the Nordik S130 softdevice
#endif

#if CONFIG_ENABLED(MICROBIT_DBG)
#error use of the serial port by MICROBIT_DBG clashes with our use of the serial port - not uspported
#endif

#define MY_DEBUG 1
#ifdef MY_DEBUG
    #define SD(format, args...)      uBit.serial.printf ("D " format "\n", ## args)
    #define SDSTART(format, args...) uBit.serial.printf ("D " format, ## args)
    #define SDCONT(args...)          uBit.serial.printf (args)
    #define SDEND                    uBit.serial.printf ("\n")
#else
    #define SD(...)
    #define SDSTART(...)
    #define SDCONT(...)
    #define SDEND
#endif

#define SPUB_EVENT(type, reason) uBit.serial.printf ("P %s %s 0x%04x:0x%04x\n", device_id, "mb\\evtsvc", type, reason)

extern char* MICROBIT_BLE_DEVICE_NAME;

/* NOTES
* XXX Would be great to have some code review by someone who knows what they're talking about - I've cargo culted most of this
*/

char *device_id = NULL; 
DiscoveredCharacteristic microbitEventCharacteristic;
DiscoveredCharacteristic clientEventCharacteristic;
bool foundMicrobitEventCharacteristic = false;
bool foundClientEventCharacteristic   = false;

uint8_t set_device_id (const char* id) {
    uint8_t changed = 0;

    if(!device_id) { device_id = (char *)malloc(6); memset(device_id, 0, 6); }

    if(memcmp(device_id, id, 5) != 0) {
        /* id changed */
        memcpy(device_id, id, 5);
        SD("Set device to '%s'", device_id);
        changed = 1;
    }

    return changed;
}

void advertisementCallback(const Gap::AdvertisementCallbackParams_t *params) {
    /* Walk the advertising data, looking for COMPLETE_LOCAL_NAME, matching "BBC MicroBit [xxxxx]"
     * and connect to this device, only if the xxxxx matches the one we are expecting.
     */
    uint8_t len = params->advertisingDataLen;
    uint8_t pos = 0;
    while(len > pos) {
        uint8_t adlen = *(params->advertisingData+pos);
        uint8_t type  = *(params->advertisingData+pos+1);
        if (type == GapAdvertisingData::COMPLETE_LOCAL_NAME) {
            if( (adlen >= 14) && (memcmp(MICROBIT_BLE_DEVICE_NAME,params->advertisingData+pos+2, 14) == 0) ) {
                /* found a micro:bit */
                if((adlen >= 14+5) && !device_id) {
                    /* haven't seen an attempt to set the name, so use the one found */
                    set_device_id((char *)(params->advertisingData+pos+2+14));
                }

                if(memcmp(device_id, params->advertisingData+pos+2+14, 5) == 0) {
                    SD("Found microbit %s", device_id);
                    if(BLE_ERROR_NONE == uBit.ble->gap().connect(params->peerAddr, Gap::ADDR_TYPE_RANDOM_STATIC, NULL, NULL)) {
                        uBit.ble->gap().stopScan();
                    }
                    return; /* we're done - if the connect failed, then we'll try again on the next advertising cycle */
                }
            }
        }
        pos = pos + adlen + 1;
    }
}

void start_ad_scan() {
    foundMicrobitEventCharacteristic = false;
    foundClientEventCharacteristic   = false;
    uBit.display.print('S'); /* Scanning */
    uBit.ble->gap().setScanParams(500, 400);
    uBit.ble->gap().startScan(advertisementCallback);
}

void discoveryTerminationCallback(Gap::Handle_t connectionHandle) {
    (void) connectionHandle; /* -Wunused-parameter */

    if (foundMicrobitEventCharacteristic && foundClientEventCharacteristic) {
        /* Request notifications */
        ble_error_t e = microbitEventCharacteristic.requestHVX(BLE_HVX_NOTIFICATION);
        if(BLE_ERROR_NONE != e) { SD("ERROR: Notification request returned: %u", e); }
        uBit.display.print('C'); /* Connected, service/characteristic scan finished, ready to do work */
    }
    else {
        /* If we haven't found the expected characcteristics, then drop the connection which will result in us
         * re-starting the scan/connect sequence */
        uBit.ble->gap().disconnect(Gap::REMOTE_USER_TERMINATED_CONNECTION);
    }
}

void characteristicDiscoveryCallback(const DiscoveredCharacteristic *characteristicP) {
    if (characteristicP->getUUID() == UUID(MicroBitEventServiceMicroBitEventCharacteristicUUID)) { 
        microbitEventCharacteristic      = *characteristicP;
        foundMicrobitEventCharacteristic = true;
    }
    if (characteristicP->getUUID() ==  UUID(MicroBitEventServiceClientEventCharacteristicUUID)) { 
        clientEventCharacteristic      = *characteristicP;
        foundClientEventCharacteristic = true;
    }
}

void connectionCallback(const Gap::ConnectionCallbackParams_t *params) {
    SD("Connected to %s", device_id);
    if (params->role == Gap::CENTRAL) {
        uBit.display.print('D'); /* Discovery phase */
        uBit.ble->gattClient().onServiceDiscoveryTermination(discoveryTerminationCallback);
        uBit.ble->gattClient().launchServiceDiscovery(params->handle, NULL ,characteristicDiscoveryCallback);
    }
}

void disconnectionCallback(Gap::Handle_t handle, Gap::DisconnectionReason_t reason) {
    (void) handle; /* -Wunused-parameter */
    (void) reason; /* -Wunused-parameter */
    /* re-start Scan */
    start_ad_scan();
}

void hvxCallback(const GattHVXCallbackParams *params) {
    int len = params->len; 
    EventServiceEvent *e = (EventServiceEvent *)params->data;

    if (params->handle == microbitEventCharacteristic.getValueHandle()) {
        /* it's an event from the connected microbit - send all the events (typically one)*/
        for (;len >= 4; len-=4, e++) {
            SPUB_EVENT(e->type, e->reason);
        }
    }
}

#define CMD_CMD    0
#define CMD_DEVICE 1
#define CMD_TOPIC  2
#define CMD_DATA   3
#define CMD_MAX    4
void process_cmd(char* s) {
    char *e = s + strlen(s);
    char *p;
    uint8_t state = 0;
    char *parts[CMD_MAX] = { NULL };

    while((s <= e) && (state < CMD_MAX)) {
        p = s;
        while((s <= e) && (*s != ' ')) { ++s; }
        *s++ = '\0';
        while((s <= e) && (*s == ' ')) { ++s; }
        parts[state++] = p;
    }

    /* Set device command */
    if( parts[CMD_CMD]    && (strlen(parts[CMD_CMD])    ==  1) && (memcmp(parts[CMD_CMD]  , "I"          , 1) == 0) &&
        parts[CMD_TOPIC]  && (strlen(parts[CMD_TOPIC])  == 10) && (memcmp(parts[CMD_TOPIC], "mb\\setname",10) == 0) &&
        parts[CMD_DEVICE] && (strlen(parts[CMD_DEVICE]) ==  5) )
    {
        uint8_t name_changed = set_device_id(parts[CMD_DEVICE]);
        /* If device id has been changed then we should drop the connectiona and re-start the scan for the new device */
        if(uBit.ble->getGapState().connected && name_changed) {
            uBit.ble->gap().disconnect(Gap::REMOTE_USER_TERMINATED_CONNECTION);
        }
    }

    /* Send Event command */
    if( parts[CMD_CMD]    && (strlen(parts[CMD_CMD])    ==  1) && (memcmp(parts[CMD_CMD]   , "I"         , 1) == 0) &&
        parts[CMD_TOPIC]  && (strlen(parts[CMD_TOPIC])  ==  9) && (memcmp(parts[CMD_TOPIC] , "mb\\evtsvc", 9) == 0) &&
        parts[CMD_DEVICE] && (strlen(parts[CMD_DEVICE]) ==  5) && (memcmp(parts[CMD_DEVICE], device_id   , 5) == 0) &&
        parts[CMD_DATA]   && (strlen(parts[CMD_DATA])   >   0) )
    {
        EventServiceEvent evt;
        char *p = parts[CMD_DATA];
        char *s;
        char *end;
        char *e = p + strlen(p);

        /* TODO Generically we should un-escape the cmd data before further processing */

        for(s=p;s<e;s++) { if(*s == ':') { *s = ' '; }} /* replace : with <space> */
        evt.type   = strtoul(p, &end, 0);
        s = end;
        evt.reason = strtoul(s, &end, 0);

        /* Validate the parsing and values, and send events back onto the event bus of the remote device */
        if (foundClientEventCharacteristic && end == e && evt.type > 0 && evt.reason > 0) {
            ble_error_t e = clientEventCharacteristic.write(sizeof(evt),(const uint8_t*)(&evt));
            if(BLE_ERROR_NONE != e) { SD("ERROR: Write request returned: %u", e); }
        }
    }
}

void serialRxCallback () {
    static char buf[100] = {};
    static uint8_t pos = 0;
    char c;

    while(uBit.serial.readable()) { /* Can this starve the rest of the program? */
        c = uBit.serial.getc();

        if(c == '\n') {
            buf[pos] = '\0';
            pos = 99;
        }
        else {
            buf[pos++] = c;
        }

        if(pos >= 99) {
            buf[99] = '\0';
            process_cmd(buf);
            memset(buf, 0, 100);
            pos = 0;
        }
    }
}

void app_main() {
    uBit.ble = new BLEDevice();
    uBit.ble->init();
    uBit.ble->gap().onDisconnection(disconnectionCallback);
    uBit.ble->gap().onConnection(connectionCallback);
    uBit.ble->gattClient().onHVX(hvxCallback);
    uBit.serial.attach(serialRxCallback);

    /* Wait until we have a device id to connect to
     * OR press button A to connect to the first found micro:bit */
    uBit.display.print('?');
    while(!device_id && !uBit.buttonA.isPressed()) {
        uBit.sleep(20);
    }

    start_ad_scan(); /* start the scan/discover/connect sequence */

    while (true) {
        uBit.ble->waitForEvent();
    }
}
