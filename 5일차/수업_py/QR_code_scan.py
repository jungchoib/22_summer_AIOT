import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(0)
sensor.set_hmirror(0) # set hmirror if can not recognize qr code
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    res = img.find_qrcodes()    # qr찾는 함수
    fps =clock.fps()
    if len(res) > 0:
        img.draw_string(2,2, res[0].payload(), color=(0,255,0), scale=5)
        print(res[0].payload()) # 함수로 얻어낸 값 출력
    lcd.display(img)

# 예시 qr code는 https://ko.qr-code-generator.com 여기서 생성가능