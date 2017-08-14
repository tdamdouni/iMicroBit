# Bluetooth MAX6675

A Bluetooth service that streams the temperature from a MAX6675 temperature probe.

## Usage

Simply call ``startMax6675Service`` with the pin where the MAX6675 is connected
to start a service that beams the temperature every second.

```blocks
bluetooth.startMax6675Service(DigitalPin.P0);
```

Then use the temperature charting from [Bitty data logger](http://www.bittysoftware.com/apps/bitty_data_logger.html) to visualize it.

## Supported targets

* for PXT/microbit
(The metadata above is needed for package search.)

```package
bluetooth
bluetooth-temperature-sensor
bluetooth-max6675
```

## License

MIT

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
