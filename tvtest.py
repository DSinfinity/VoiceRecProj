import cec
import time
cec.init()
tv = cec.device(0)
time.sleep(5)
tv.power_on()
time.sleep(30)
tv.standby()