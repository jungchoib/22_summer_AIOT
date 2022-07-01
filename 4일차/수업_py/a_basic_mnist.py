import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()  # # 케라스의 mnist의 데이터셋을 로드

# 데이터 확인해보기
plt.imshow(x_train[0], cmap='gray') # 배열 x_train를 이미지로 변환
y_train[0] # x_train의 정답값
x_train.shape # 반환값:(60000, 28, 28) -> 28X28(2D) 가 6만개    / 따라서 Denselayer 넣기위해 1D로 flatten필요

# 1D만들기 위한 flatten화
x_train, x_test = x_train.reshape(-1, 28 * 28), x_test.reshape(-1, 28 * 28) # 1줄에 28*28개로 1D로 flatten됨

y_train, y_test = tf.keras.utils.to_categorical(y_train), tf.keras.utils.to_categorical(y_test)
# y(답)의 형태와 output 모양 같게하기위해 수정필요

x_train, x_test = x_train / 255.0, x_test / 255.0
# x의 max값이 255로 너무 커서 0~1사이값 만들어주기


# model만들기
model = tf.keras.models.Sequential()    # sequential: 앞에서 차례대로 읽는 모델
model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
                        # Dense=fully connected layer ->1D
                                # loss함수(cross or 린스퀘어에러)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            # 최적화(adam=gradient decsent버전)                     평가 지표
model.summary() # 로 정리한거 보여줌    잘 설계됫나 확인하기 좋음
# summary의 응답값
''' Model: "sequential"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense (Dense)                (None, 64)                50240     Dense layer 1개 지나가면 64개 output
    _________________________________________________________________
    dense_1 (Dense)              (None, 10)                650       Dense layer 1개 지나가면 10개 output
    =================================================================
    Total params: 50,890
    Trainable params: 50,890
    Non-trainable params: 0
    _________________________________________________________________
'''
# 모델 학습                 과부화 방지 64개 1묶음씩    10번 에포크 반복
model.fit(x_train, y_train, batch_size=64, epochs=10,
          validation_data=(x_test, y_test))
# 모델학습의 응답값
'''
    Train on 60000 samples, validate on 10000 samples
    Epoch 1/10                                                      train값의 오차율      test값의 오차율
    60000/60000 [==============================] - 7s 110us/sample - loss: 0.3460 - val_loss: 0.1979
'''
# 직접 예측
test_prediction = model.predict(x_test) # 특정 문제만 풀고싶으면 reshape로 크기 맞추는것도 필요함
# reshape 예시
test_prediction = model.predict(x_test[0].reshape(-1, 784))

test_prediction
# 배열속 인자에 각각의 확률이 나옴  ex) 7번쨰 항이 0.99면 7이 정답일 확률이 99%임을 뜻함