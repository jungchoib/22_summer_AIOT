# 카메라를 LCD에 출력
import sensor, image, time, lcd

sensor.reset()                      
sensor.set_pixformat(sensor.RGB565) # 표현 색
sensor.set_framesize(sensor.QVGA)   # 픽셀사이즈 QVGA = 320X240
sensor.skip_frames(time = 2000)     # 딜레이

lcd.init(freq=15000000)             # 1초에150000000번 깜빡
clock = time.clock()                

while(True):
    clock.tick()                    
    img = sensor.snapshot()         # img에 카메라찍은거 지정
    lcd.display(img)                
    print(clock.fps())              # fps = Flame Per Second
                                    
# LCD에 글씨쓰기
import image, lcd

lcd.init()

lcd.draw_string(0, 0, "hello")  # 0,0은 위치    그냥 출력

img = image.Image(size=(320, 240))  # 글자를 이미지형으로 출력
img.draw_string(0, 0, "hello")    # 얘가 써먹기 좋음
lcd.display(img)

# 여러 image 띄우기 예시
import image, lcd, utime

lcd.init()
img = image.Image()
                        # 100크기로                 color로 채우기 T
img.draw_circle((100, 100, 100), color=(0, 255, 0), fill=True)
lcd.display(img) # 100,100위치에
utime.sleep(1)
                         # 사각형이라 200X70
img.draw_rectangle((100, 100, 200, 70), color=(255, 0, 0), fill=True)
lcd.display(img)
utime.sleep(1)
                    # lcd크기(폭, 높이)불러옴
img.draw_line((0, 0, lcd.width(), lcd.height()), thickness=3, color=(0, 0, 255))
lcd.display(img)
utime.sleep(1)

img.draw_string(100, 100, 'hi', scale=2)
lcd.display(img)
utime.sleep(1)

# find blobs 블롭함수 이용해서 색깔찾기
# 실행 방법은 강의자료보고 Treshold editor에 LAB(L은 밝기 / A: +red -green / B: +yello -blue)이용하여 찾아낸값에 넣기
import sensor, image, lcd, time
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)   # 카메라 돌아가라

blob_threshold = (4, 49, 78, 8, -114, -42)  # 찾아낼 값 (Treshold editor이용하여 찾기 )
while True:
    img=sensor.snapshot()   # 카메라의 이미지 받아오고
    blobs = img.find_blobs([blob_threshold])    # find_blobs함수 사용
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])  # blob찾는 값중 0~4는 크기
            tmp=img.draw_cross(b[5], b[6])  #           5, 6은 중앙위치나타냄
            c=img.get_pixel(b[5], b[6])
            lcd.display(img)