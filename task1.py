from gpiozero import Button
from gpiozero import LED
from time import sleep

button=Button(3) 
led = LED(2)
clicks = 0

while True:
    if button.is_pressed:
        clicks+=1
        sleep(0.5)
    if clicks %2 != 0:
        led.on()
    elif clicks % 2 == 0:
        led.off()
        
             
