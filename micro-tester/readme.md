#Micro:tester: easily test the range of the radio on your micro:bit

The NRF51822 SoC that is used in the micro:bit enables wireless communication on the 2.4GHZ band between compatible devices - E.G. 2 (or more) micro:bits. Whilst said functionality is normally rather reliable, in practice, radio communication in general is often affected by a large number of external factors which may drrasticly ulter its range / reliability, impacting its usefulness accordingly.

Micro:tester consists of 2 small Python scripts to assist in testing the range / reliability of the radio functionality using 2 micro:bits. Having run various micro:bit-theamed events that have been heavily reliant on radio working properly & experienced the pain of it not, I observed that a simplistic example that tests the core Tx/Rx functionality without any event-specific features would be a useful tool to deploy during setup to determine what issues I may run into during the event.