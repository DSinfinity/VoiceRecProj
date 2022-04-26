import speech_recognition as sr
import time
#import cec
from gpiozero import LED

INITIAL = "ok tv"
TV_ON = "turn on"
TV_OFF = "turn off"
CLOSE = "stop"

red = LED(17)
green = LED(27)
blue = LED(22)


def detect():
    #cec.init()
    r = sr.Recognizer()
    #tv = cec.Device(0)
    

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            blue.on()
            aud = r.record(source,duration=5)
            try:
                txt = r.recognize_google(aud,language="en-GB")
                
            except sr.UnknownValueError:
                print("None")
                blue.off()
                red.on()
                time.sleep(1)
                red.off()
                continue

            blue.off()
            green.on()
            time.sleep(1)
            green.off()
            print(txt)

            if INITIAL not in txt.lower():
                print("not Active")
                red.on() 
                time.sleep(0.5)
                red.off()
                time.sleep(0.5)
                continue
            else:
                print("detected")
                green.on()
                time.sleep(0.5)
                green.off()
                while True:

                    cmd = r.record(source,duration = 3)
                    try:
                        txt2 = r.recognize_google(cmd,language="en-GB")
                        print(txt2)
                        if TV_ON in txt2.lower():
                            print ("turning On")
                            green.on()
                            blue.on()
                            #tv.power_on()
                            time.sleep(5)
                            green.off()
                            blue.off()
                            break

                        elif TV_OFF in txt2.lower():
                            print ("turning OFF!")
                            green.on()
                            red.on()
                            #tv.standby()
                            time.sleep(5)
                            green.off()
                            red.off()
                            break

                        elif CLOSE in txt2.lower():
                            green.on()
                            blue.on()
                            red.on()
                            print ("Stopping program")
                            time.sleep(5)
                            green.off()
                            red.off()
                            blue.off()
                            break
                        else:
                            print("not detected")
                            red.on()
                            time.sleep(5)
                            red.off()
                            break
        
                    except sr.UnknownValueError:
                        print ("failed")
                        red.on()
                        time.sleep(0.5)
                        red.off()
                        time.sleep(0.5)
                        red.on()
                        time.sleep(0.5)
                        red.off()
                        time.sleep(0.5)
                        break
                    break



while True:
    detect()
                
    
        


