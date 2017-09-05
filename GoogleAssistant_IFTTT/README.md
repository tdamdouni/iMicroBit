# GoogleAssistant_IFTTT
Control the micro:bit LED matrix with IFTTT, Google Assistant and NodeJS app. 

In the previous project, I created the Google Assistant demo to control the micro:bit LED lights with Webhook and API.ai. I found a simple way to do it (simple means less configurations and programming). 

In this demo, I use IFTTT and created two applets:
1. "If you say 'off the light' then make a web request"
2. "If you say 'on the light' then make a web request"

On the other part (Raspberry Pi/Linux Ubuntu), I created a simple NodeJS app to capture the POST request from IFTTT with the help of
Ngrok and from there control the micro:bit LED matrix from bluetooth event service.

With this configuration, you can straightaway tell Google Assistant to on and off the light. You don't need to ask Google Assistant to trigger the companion app (like in the previous project, you need to say 'OK Google, talk to my test app' and then ask Assistant to on and off the light).

On the micro:bit, you can do whatever you want instead of controlling the light, you can control motor, actuator, etc.
