# ADC = Analog to Digital Converter

# 가변저항 연결
from itertools import count
import time, network
from Maix import GPIO
from fpioa_manager import fm

class wifi():                                                   # 이부분은 K210에서 바로 사용 못하고
    # IO map for ESP32 on Maixduino                             # (ADC: 아날로그 신호 사용)ESP32에서 변환해서 사용해야하므로
    fm.register(25, fm.fpioa.GPIOHS10)  # cs                    # 통신으로 변환하는 과정
    fm.register(8, fm.fpioa.GPIOHS11)   # rst
    fm.register(9, fm.fpioa.GPIOHS12)   # rdy
    print("Use Hardware SPI for other maixduino")
    fm.register(28, fm.fpioa.SPI1_D0, force=True)   # mosi    
    fm.register(26, fm.fpioa.SPI1_D1, force=True)   # miso
    fm.register(27, fm.fpioa.SPI1_SCLK, force=True) # sclk
    nic = network.ESP32_SPI(cs=fm.fpioa.GPIOHS10, rst=fm.fpioa.GPIOHS11, rdy=fm.fpioa.GPIOHS12, spi=1)  # 여기까지가 변환

print("ESP32_SPI firmware version:", wifi.nic.version())
 
while True:
    try:
        #get ADC0~5
        adc = wifi.nic.adc((0,))    # [0]도 가능, 자료 3개면 (0, 1, 2)
    except Exception as e:
        print(e)
        continue
    for v in adc:
        print("ADC0 Value : %04d" %(v))    # 위의 튜플값 읽기위한 for문


# 초음파센서 연결
from fpioa_manager import fm
from Maix import GPIO
import utime
from machine import Timer

count = 0
def on_timer(timer):
    global count        # falling edge = 진동멈추고 타이머 시작
    count = count + 1   # 따라서 count +1마다 20ms 지남

def test_irq(pin_num):  # 다시 신호 받을때 이거 실행
    global count        
    tim.stop()
    if count > 10:      # 노이즈는 무시하기위해 count허들 설정 
        print((340*count)/1000)/2
    count = 0
def ultra_send():
    for _ in range(8):
        trig.value(1)       # 1->0 진동보낸거
        utime.sleep_us(10)  # falling edge는 진동보낸거 멈춘거
        trig.value(0)
        utime.sleep_us(10)
    tim.start()

io_echo_pin = 14    # 회로도 8
io_trig_pin = 13    # 9번 
fm.register(io_echo_pin, fm.fpioa.GPIOHS0) # HS = High Speed
fm.register(io_trig_pin, fm.fpioa.GPIO0)

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=20, unit=Timer.UNIT_US, callback=on_timer, arg=on_timer)
print("period", tim.period())                       # 주기적 실햄        20                  ms 마다       on_timer함수 실행

echo = GPIO(GPIO.GPIOHS0, GPIO.IN)
trig = GPIO(GPIO.GPIO0, GPIO.OUT)                       # 10은 우선수위
echo.irq(test_irq, GPIO.IRQ_FALLING, GPIO.WAKEUP_NOT_SUPPORT,10)    # interrupt방해하다
                    # Falling edge(급락할떄)마다 test_irq함수사용
while True:     # while문은 디바이스 여유될때마다만 반복->시간측정 부정
    ultra_send()            # 따라서 Timer함수 사용함
    utime.sleep(1)