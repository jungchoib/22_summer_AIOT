from fpioa_manager import fm

fm.register(11, fm.fpioa.GPIO0, force=True)     # K210 11핀을 등록 GPIO0기능으로 사용
fm.register(12, fm.fpioa.GPIOHSO0, force=True)  # force 는 12번핀이 다른일 하고 있어도 강제로 지금일 주려고씀
fm.register(13, fm.fpioa.UART2_TX)              # GPIO(General Purpose Input Output)
fm.register(14, fm.fpioa.UART2_RX)

# other code

fm.unregister(11)   # 위의 기능사용이 끝나면 등록해재
fm.unregister(12)
fm.unregister(13)
fm.unregister(14)

# LED 깜빡이기
from fpioa_manager import fm
from Maix import GPIO
import utime
io_led_red = 15
fm.register(io_led_red, fm.fpioa.GPIO0)     # 15pin = GPIO0으로 사용

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)      # OUT으로 사용

while(True):
    led_r.value(1)          # value 1=ON / 0=OFF
    utime.sleep_ms(1000)    # utime = 마이크로 초
    led_r.value(0)
    utime.sleep_ms(1000)