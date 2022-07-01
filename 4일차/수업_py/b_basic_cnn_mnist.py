import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

############# Data Preparation
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

y_train, y_test = tf.keras.utils.to_categorical(y_train), tf.keras.utils.to_categorical(y_test)


######### Model build                                   그 전에 convolution 과 pulling 필요
model = tf.keras.models.Sequential([    # flatten X? ->layer로 안가고 이미지 자체를 쓰기때문에 reshape 안함
    tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)), # 28x28                 (3,3)이라 양쪽 1개씩 사라져서 26*26됨
    tf.keras.layers.Conv2D(16, kernel_size=(3, 3), padding='VALID', activation='relu'), #26x26X16  convolution
                        # 16은 이미지의 output 갯수                                                                     AXAXB A는 행렬, B는 feature map
    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), padding='VALID', activation='relu'), #24x24X32 얘는 4,4가
    tf.keras.layers.MaxPool2D((2, 2)), #12x12X32       = 패딩은 없음    0과1 표현법?                    2,2되서 절반인 12X12됨
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), padding='VALID', activation='relu'), #10x10X64
    tf.keras.layers.Flatten(),  # 여기서 flatten                                        inout이 6400개
    tf.keras.layers.Dense(1024, activation='relu'), # 여기서 뉴럴 시작  1024개
    tf.keras.layers.Dense(10, activation='softmax') #   뉴럴의 output 10개
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

#### Training
model.fit(x_train, y_train, batch_size=256, epochs=10,
          validation_data=(x_test, y_test),)

# 직접 예측
test_prediction = model.predict(x_test) # 특정 문제만 풀고싶으면 reshape로 크기 맞추는것도 필요함
# reshape 예시
test_prediction = model.predict(x_test[0].reshape(-1,28,28))
