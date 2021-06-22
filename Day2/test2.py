from pop import Pilot
from pop import LiDAR
from gtts import gTTS

import subprocess
import math
import random

SPEED = 50
direction = 0

lidar = LiDAR.Rplidar()
bot = Pilot.SerBot()

lidar.connect()
lidar.startMotor()

bot.setSpeed(SPEED)

text = "시작합니다."
filename = "en_tts.mp3"

# tts = gTTs(text, lang='ko') 
# tts.save(filename)

# with subprocess.Popen(['play', 'en_tts.mp3']) as p: #Popen([리눅스 명령어, filename])
#     p.wait()
while True:
    
    vectors = lidar.getVectors()
    for v in vectors:
        #degree = v[0]    # 각도
        #distance = v[1]  # 거리

        if 0 < v[0] < 45:
            if v[1] < 700:
                print("45도 안")

        elif 325 < v[0] < 360:
            if v[1] < 700:
                
                print("-45도 안")