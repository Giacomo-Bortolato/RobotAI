from arduino.app_utils import App,Bridge
import time

led_state=1
time.sleep(1)
def loop():
    global led_state

    Bridge.call("Risposta",led_state)
    time.sleep(5)
    led_state=0
    Bridge.call("Risposta",led_state)
    time.sleep(5)
    led_state=1




App.run(user_loop=loop)
