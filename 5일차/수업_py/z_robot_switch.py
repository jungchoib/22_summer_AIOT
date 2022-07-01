import sensor, image, lcd, time
from Maix import GPIO
from fpioa_manager import fm
from board import board_info
from machine import Timer,PWM
import utime
import gc, sys

lcd.init()

# PWM이용하여 모테의 세기 조절위한 시작
tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
tim3 = Timer(Timer.TIMER0, Timer.CHANNEL2, mode=Timer.MODE_PWM)
tim4 = Timer(Timer.TIMER0, Timer.CHANNEL3, mode=Timer.MODE_PWM)

# pin번호 잘 맟추기
ch1 = PWM(tim1, freq=256, duty=50, pin=24)
ch2 = PWM(tim2, freq=256, duty=50, pin=32)
ch3 = PWM(tim3, freq=256, duty=50, pin=13)
ch4 = PWM(tim4, freq=256, duty=50, pin=12)

duty = 0    # 0으로 초기화
ch1.duty(duty)
ch2.duty(duty)
ch3.duty(duty)
ch4.duty(duty)

# 버튼 부분
fm.register(21, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN ,GPIO.PULL_UP) # pull up = 항상 1인상태

# 강의자료 모턷라이브 보면  H L 정방향 / L H 역방향 / LH LH 정지    Low(0) High(1)나타냄
def straight():
    ch1.duty(0)
    ch2.duty(90)        # 여기서 숫자는 출력 속도 나타냄 따라서 100넣으면 더 빨라짐
    ch3.duty(90)
    ch4.duty(0)

def right_move():
    ch1.duty(0)
    ch2.duty(90)
    ch3.duty(0)
    ch4.duty(0)

def left_move():
    ch1.duty(0)
    ch2.duty(0)
    ch3.duty(90)
    ch4.duty(0)

def stop():
    ch1.duty(0)
    ch2.duty(0)
    ch3.duty(0)
    ch4.duty(0)

sensor_window=(224, 224)    # 카메라로 찍은 데이터값의 크기 224X224
lcd_rotation=0
sensor_hmirror=False        # 카메라 수평반전
sensor_vflip=False          # 카메라 수직반전

# 카메라 세팅
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing(sensor_window)
sensor.set_hmirror(sensor_hmirror)
sensor.set_vflip(sensor_vflip)
sensor.run(1)

# LCD세팅
lcd.init(type=1)
lcd.rotation(lcd_rotation)
lcd.clear(lcd.WHITE)

# 이미지 받아서 표현하기
try:
    img = sensor.snapshot()
    lcd.display(img)
except Exception:
    img = image.Image(size=(320, 240))
    lcd.display(img)

state_previous = 1
count = 0
try:
    while(True):    # 버튼누르면 멈추는 함수
        img = sensor.snapshot()
        state_current = btn.value()
        if state_current == 0:
            if state_previous == 1:
                count = count + 1
                state_previous = 0
                stop()
                img.clear()
                img.draw_string(100,100,"END", color=(255, 0, 0),scale=4)
                lcd.display(img)
                break
            utime.sleep_ms(100)

        straight()  # 작동하면 직진상태 /   버튼 누르면 위의 count=1되서 정지함
        lcd.display(img)

except Exception as e:
    sys.print_exception(e)
