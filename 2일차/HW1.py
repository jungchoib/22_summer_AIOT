# 1. 4개 동시 깜빡

from fpioa_manager import fm
from Maix import GPIO
import utime
io_led_red = 15     # 7번
io_led_green = 32   # 6번
io_led_blue = 24    # 5번
io_led_green_2 = 23 # 4번

fm.register(io_led_red, fm.fpioa.GPIO0)     # 15pin = GPIO0으로 사용
fm.register(io_led_green, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)
fm.register(io_led_green_2, fm.fpioa.GPIO3)

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)      # OUT으로 사용
led_g = GPIO(GPIO.GPIO1, GPIO.OUT)
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)
led_g_2 = GPIO(GPIO.GPIO3, GPIO.OUT)

while(True):
    led_r.value(1)          # value 1=ON / 0=OFF
    led_g.value(1)
    led_b.value(1)
    led_g_2.value(1)
    utime.sleep_ms(1000)    # utime = 마이크로 초
    led_r.value(0)
    led_g.value(0)
    led_b.value(0)
    led_g_2.value(0)
    utime.sleep_ms(1000)




# 2. 1개씩 돌아가면서 켜기

from fpioa_manager import fm
from Maix import GPIO
import utime
io_led_red = 15     # 7번
io_led_green = 32   # 6번
io_led_blue = 24    # 5번
io_led_green_2 = 23 # 4번

fm.register(io_led_red, fm.fpioa.GPIO0)     # 15pin = GPIO0으로 사용
fm.register(io_led_green, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)
fm.register(io_led_green_2, fm.fpioa.GPIO3)

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)      # OUT으로 사용
led_g = GPIO(GPIO.GPIO1, GPIO.OUT)
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)
led_g_2 = GPIO(GPIO.GPIO3, GPIO.OUT)

a=1
b, c, d = 0, 0, 0

while(True):
    if a==1:
        a, b, c, d = 0, 1, 0, 0
    elif b==1:
        a, b, c, d = 0, 0, 1, 0
    elif c==1:
        a, b, c, d = 0, 0, 0, 1
    else:
        a, b, c, d = 1, 0, 0, 0
    led_r.value(a)          # value 1=ON / 0=OFF
    led_g.value(b)
    led_b.value(c)
    led_g_2.value(d)
    utime.sleep_ms(1000)    # utime = 마이크로 초