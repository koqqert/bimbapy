import tensorflow as tf #машинное обучение
import numpy as np #математика
import matplotlib.pyplot as plt #графика

from tensorflow.keras.datasets import mnist #библиотека с цифрами
from tensorflow.keras.models import Sequential #модель
from tensorflow.keras.layers import Dense, Flatten #слои
from tensorflow.keras.utils import to_categorical #векторизация

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test = x_test / 255

y_train = to_categorical(y_train, 10) 
y_test = to_categorical(y_test, 10)

model = Sequential([ #создание модели
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', #компиляция модели
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=15) #обучение модели

model.save('mnist_model.keras') #сохранение модели

k = 6
plt.imshow(x_test[k])
plt.axis('off')
print(y_test[k])


