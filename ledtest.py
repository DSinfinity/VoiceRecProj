#gpio: 17-red  27-green  22-blue
from gpiozero import LED
import time

red = LED(17)
green = LED(27)
blue = LED(22)

time.sleep (2)
red.on()
green.on()
blue.on()

time.sleep(0.5)
red.off()
time.sleep(0.5)
red.on()
time.sleep(0.5)
red.off()
green.off()
blue.off()

