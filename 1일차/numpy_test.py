# 1. anacona 설치 후 cmd열기
# 2. conda create -n aiot python=3.7 입력   => aiot라는 3.7버젼파이썬을 가진 가상환경 생성
#   + conda (de)activate aiot로 껏다켜기 가능
# 3. aiot환경에서   conda install jupyter notebook 입력으로 주피터노트북 생성(텐서플로우등 깔기쉬운거 사용)
# 4. aiot환경에서   conda install tensorflow 입력으로 텐서플로우 설치
# 5. aiot환경에서 jupyter notebook 으로 주피터노프북 접속(웹으로)

from numpy import *
print(random.rand(4,4))
import tensorflow as tf

# mnist(숫자인식) 훈련 & 테스트
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test)=mnist.load_data() # x이미지 y정답값
x_train, x_test = x_train/255.0, x_test/255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)), # size28X28, flat하게 펴준다
    tf.keras.layers.Dense(128,activation='relu'), # 여기를 통과하면 128개로 줄어든다 relu=0에 수렴을 방지
    tf.keras.layers.Dropout(0.2),                 # 20% 없애준다.
    tf.keras.layers.Dense(10,activation='softmax') # 10개로 줄인다.
])

model.compile(optimizer='adam',  # 경사하강법
             loss='sparse_categorical_crossentropy',  # 10개의 관문을 사용하겟다.
             metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5,batch_size=1) # epoch반복학습 횟수(너무 많아도 안좋음)  batch_size=파워가 부족해서epoch를 나눠서 입력

model.evaluate(x_test,y_test)