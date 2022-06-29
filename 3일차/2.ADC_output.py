# PWM = Palse Width Modulation 디지털로 아날로그출력모방
# input과 다르게 output은 k210 이용 가능!

# 숨쉬는 LED
from machine import Timer, PWM
import time
import random
tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
tim3 = Timer(Timer.TIMER0, Timer.CHANNEL2, mode=Timer.MODE_PWM)

ch1 = PWM(tim1, freq=500000, duty=50, pin=21)
ch2 = PWM(tim2, freq=500000, duty=50, pin=22)
ch3 = PWM(tim3, freq=500000, duty=50, pin=23)
duty=0
dir = True
while True:
    if dir:
        duty +=2
    else:
        duty -=2
    if duty>100:
        duty = 100
        dir = False
    elif duty<0:
        duty = 0
        dir = True
    time.sleep_ms(50)
    ch1.duty(duty)
    ch2.duty(duty)
    ch3.duty(duty)

# 서보 모터 구돌     DC모터: 연속회전(제어어렵)    서보 모터: 제어가능 + DC모터   스텝모터: 정밀조정
#   1ms = 0도     1.5ms = 90도    2ms = 180도
from machine import Timer, PWM
import utime
def servo_angle(angle): # 우리서보모터의 경우 0.5ms ~ 2.5ms이기때문에      angle: -90 ~ 90
    duty = ((angle+90)/180*10+2.5)  # 2.5= 10duty(2ms)의 1/4(0.5ms)
    return duty
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=50, duty=0, pin=11)
            # 50ㄹfreq=20ms        # 11번 자리가 우연히 11
while True:
    ch.duty(servo_angle(90)) # 여기각도로 바뀌는거임
    print(servo_angle(90))
    utime.sleep_ms(5)


# 부저 출력
from fpioa_manager import fm
from machine import Timer, PWM
import utime
from Maix import GPIO

io_btn = 24

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=261, duty=50, pin=22)
fm.register(io_btn, fm.fpioa.GPIO0)
btn = GPIO(GPIO.GPIO0, GPIO.IN, GPIO.PULL_UP)
                    # 버튼in    ground라 pull up : 눌리면 0됨
um = [261, 293, 329, 349, 391, 440, 493]
    # [도 레 미 파 솔 라 시]
while True:
    if btn.value() == 0:
        ch.duty(50)
        for i in um:
            ch.freq(i)
            utime.sleep_ms(500)
    else:
        ch.duty(0)