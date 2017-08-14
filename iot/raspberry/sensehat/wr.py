from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

try:
  while True:
    sense.load_image("wr.png")

except KeyboardInterrupt:
    sense.clear()