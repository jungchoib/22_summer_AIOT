# 1. 버튼누를때마다 1개씩 4개돌아가며 켜짐
from fpioa_manager import fm
from Maix import GPIO
import utime

io_led_red = 15     # 7번
io_led_green = 32   # 6번
io_led_blue = 24    # 5번
io_led_green_2 = 23 # 4번
io_btn = 22         # 3번


fm.register(io_led_red, fm.fpioa.GPIO0)     # 15pin = GPIO0으로 사용
fm.register(io_led_green, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)
fm.register(io_led_green_2, fm.fpioa.GPIO3)
fm.register(io_btn, fm.fpioa.GPIO4)     # 22pin = GPIO0으로 사용

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)      # OUT으로 사용
led_g = GPIO(GPIO.GPIO1, GPIO.OUT)
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)
led_g_2 = GPIO(GPIO.GPIO3, GPIO.OUT)
btn = GPIO(GPIO.GPIO4, GPIO.IN, GPIO.PULL_DOWN)      # IN으로 사용



count = 0
while(True):
    state_current = btn.value()     # 0>1  바뀔때 세기
    if state_current ==1:
        if state_previous == 0:
            count = count + 1
            state_previous = 1
            print(count)
            if count%4 ==0:
                a, b, c, d = 1, 0, 0, 0
            elif count%4==1:
                a, b, c, d = 0, 1, 0, 0
            elif count%4==2:
                a, b, c, d = 0, 0, 1, 0
            else:
                a, b, c, d = 0, 0, 0, 1
            led_r.value(a)          # value 1=ON / 0=OFF
            led_g.value(b)
            led_b.value(c)
            led_g_2.value(d)
        utime.sleep_ms(100)         # 사람이 누를수 있는 최소의 시간
    else:
        state_previous = 0





# 2. cnt수마다 켜지는 갯수 다르게
count = 0
while(True):
    state_current = btn.value()     # 0>1  바뀔때 세기
    if state_current ==1:
        if state_previous == 0:
            count = count + 1
            state_previous = 1
            print(count)
            if count==0:
                a, b, c, d = 0, 0, 0, 0
            elif count%4 ==0:
                a, b, c, d = 1, 1, 1, 1
            elif count%4==1:
                a, b, c, d = 1, 0, 0, 0
            elif count%4==2:
                a, b, c, d = 1, 1, 0, 0
            else:
                a, b, c, d = 1, 1, 1, 0
            led_r.value(a)          # value 1=ON / 0=OFF
            led_g.value(b)
            led_b.value(c)
            led_g_2.value(d)
        utime.sleep_ms(100)         # 사람이 누를수 있는 최소의 시간
    else:
        state_previous = 0