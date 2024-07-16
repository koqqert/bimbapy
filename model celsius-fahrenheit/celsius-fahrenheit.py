import tensorflow as tf
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

model = Sequential([
    Dense(units=1, input_shape=[1])
])
model.compile(loss = 'mean_squared_error', optimizer = tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius, fahrenheit, epochs=850, verbose=False)

model.save('celsius_fahrenheit_model.h5')
