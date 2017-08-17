"use strict";

var Service, Characteristic;
var temperatureService;
var lightbulbService;
var humidityService;
var request = require("request");
var BBCMicrobit = require('bbc-microbit')


var EVENT_FAMILY = 8888;
var EVENT_VALUE_ANY = 0;

var microbit_;

console.log('Scanning for microbit');
BBCMicrobit.discover(function(microbit) {
    console.log('\tdiscovered microbit: id = %s, address = %s', microbit.id, microbit.address);


    microbit.on('event', function(id, value) {
        console.log('\ton -> micro:bit event received event: %d value: %d', id, value);
    });

    microbit.on('disconnect', function() {
        console.log('\tmicrobit disconnected!');
        process.exit(0);
    });

    console.log('connecting to microbit');
    microbit.connectAndSetUp(function() {
        console.log('\tconnected to microbit');
        console.log('subscribing to event family, any event value');
        microbit.subscribeEvents(EVENT_VALUE_ANY, EVENT_FAMILY, function() {
            console.log('\tsubscribed to micro:bit events of required type');
        });

        microbit_ = microbit;
    });

});




module.exports = function(homebridge) {
    Service = homebridge.hap.Service;
    Characteristic = homebridge.hap.Characteristic;
    homebridge.registerAccessory("homebridge-microbit", "microbit", microbitAccessory);
};

function microbitAccessory(log, config) {
    this.log = log;
    this.name = config["name"];

}

microbitAccessory.prototype = {

    Request: function(callback) {
        callback()
    },

    setPowerState: function(powerOn, callback) {
        if (powerOn) {
            microbit_.writeEvent(1, 8888, function() {
                console.log('On');
            });
        } else {
            microbit_.writeEvent(2, 8888, function() {
                console.log('Off');
            });
        };

        this.Request(function() {
            callback();
            
        }.bind(this));
    },

    identify: function(callback) {
        this.log("Identify requested");
        callback();
    },

    getServices: function() {
        var informationService = new Service.AccessoryInformation();

        informationService
            .setCharacteristic(Characteristic.Manufacturer, "microbit")
            .setCharacteristic(Characteristic.Model, "FD18")
            .setCharacteristic(Characteristic.SerialNumber, "FD18");

        lightbulbService = new Service.Lightbulb(this.name);
        lightbulbService
            .getCharacteristic(Characteristic.On)
            .on('set', this.setPowerState.bind(this));
            



        return [informationService,
            lightbulbService
        ];


    },


};