from fpioa_manager import fm
from Maix import GPIO
import utime

io_btn = 22     # 3번자리
fm.register(io_btn, fm.fpioa.GPIO0)     # 22pin = GPIO0으로 사용

btn = GPIO(GPIO.GPIO0, GPIO.IN)      # IN으로 사용

while(True):
    btn_state = btn.value()         # value 1=ON / 0=OFF
    print(btn_state)                # 연결안되도 외부환경때문에 0.3정도 불안한 상태라 꺼져도 0/1왔다갔다 함
                                    # 따라서 pulldown으로 0.3을 0으로 내리기 / pull up은 1로 올라간다	저항을 사용하면 가능
                                    # 그러나 GPIO는 소프트웨어로 처리 가능

# pulldown 보정 & 버튼횟수 세기
from fpioa_manager import fm
from Maix import GPIO
import utime

io_btn = 22
fm.register(io_btn, fm.fpioa.GPIO0)     # 22pin = GPIO0으로 사용

btn = GPIO(GPIO.GPIO0, GPIO.IN, GPIO.PULL_DOWN)      # IN으로 사용
count = 0
while(True):
    state_current = btn.value()     # 0>1  바뀔때 세기
    if state_current ==1:
        if state_previous == 0:
            count = count + 1
            state_previous = 1
            print(count)
        utime.sleep_ms(100)         # 사람이 누를수 있는 최소의 시간
    else:
        state_previous = 0