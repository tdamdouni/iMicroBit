'use strict'

const express = require('express')
const bodyParser = require('body-parser')
const request = require('request')
const app = express()
const BBCMicrobit = require('bbc-microbit')

const EVENT_FAMILY = 8888;
const EVENT_VALUE_ANY = 0;

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

app.set('port', (process.env.PORT || 8080))

// Process application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: false}))

// Process application/json
app.use(bodyParser.json())

// Index route
app.get('/', function (req, res) {
    res.send('Hello world, I am micro:bit Singapore')
})

app.get('/webhook/', function (req, res) {
	res.sendStatus(200);
})

app.post('/webhook/', function (req, res) {
	let msg = JSON.parse(JSON.stringify(req.body));
	console.log(msg.light);

	if(msg.light == 'on') 
		microbit_.writeEvent(1, 8888, function() {
        	console.log('Light is on');
        });

	if(msg.light == 'off') 
		microbit_.writeEvent(2, 8888, function() {
        	console.log('Light is off');
        });

    res.sendStatus(200)
})

// Spin up the server
app.listen(app.get('port'), function() {
    console.log('running on port', app.get('port'))
})

