import BlynkLib
from pop import Pilot, LiDAR
import random
import time

BLYNK_AUTH = 'Z9rZjLjIkSz63o1zvuFtyfJapf7L4afq'
blynk = BlynkLib.Blynk(BLYNK_AUTH)  # server = '10.10.11.57, port=9443


bot = Pilot.SerBot()

@blynk.VIRTUAL_WRITE(0)
def go_button(n):
    print(n)
    for i in n:
        if i == '0'or i== '1':
            bot.move(0, 40)
            print("이동")


@blynk.VIRTUAL_WRITE(1)
def go_button2(n):
    print(n)
    for i in n:
        if i == '0'or i== '1':
            time.sleep(1)
            bot.stop()
            print("정지")


while True:
    try:
        blynk.run()
    except IOError:
        pass