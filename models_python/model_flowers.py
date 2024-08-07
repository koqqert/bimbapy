import os
import glob
import shutil
import numpy as np
import matplotlib.pyplot as plt

import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Dense, Flatten, Dropout

#импортируем и нормализуем данные
_URL = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
zip_file = keras.utils.get_file(origin=_URL, fname="flower_photos.tgz", extract=True)

base_dir = os.path.join(os.path.dirname(zip_file), "flower_photos",)
classes = ['roses', 'daisy', 'dandelion', 'sunflowers', 'tulips']


for cl in classes:
  img_path = os.path.join(base_dir, cl)
  images = glob.glob(img_path + '/*.jpg')
  print("{}: {} изображений".format(cl, len(images)))
  train, val = images[:round(len(images)*0.8)], images[round(len(images)*0.8):]

  for t in train:
    if not os.path.exists(os.path.join(base_dir, 'train', cl)):
      os.makedirs(os.path.join(base_dir, 'train', cl))
    shutil.move(t, os.path.join(base_dir, 'train', cl))

  for v in val:
    if not os.path.exists(os.path.join(base_dir, 'val', cl)):
      os.makedirs(os.path.join(base_dir, 'val', cl))
    shutil.move(v, os.path.join(base_dir, 'val', cl))

train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
#расширение данных
batch_size = 100
IMG_SHAPE = 150

#горизонтальный переворот
image_gen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
train_data_gen = image_gen.flow_from_directory(batch_size=batch_size, directory=train_dir, shuffle=True, target_size=(IMG_SHAPE,IMG_SHAPE))
#произвольный переворот
image_gen = ImageDataGenerator(rescale=1./255, rotation_range=45)
train_data_gen = image_gen.flow_from_directory(batch_size=batch_size, directory=train_dir, shuffle=True, target_size=(IMG_SHAPE,IMG_SHAPE))
#увеличение
image_gen = ImageDataGenerator(rescale=1./255, zoom_range=0.5)
train_data_gen = image_gen.flow_from_directory(batch_size=batch_size, directory=train_dir, shuffle=True, target_size=(IMG_SHAPE,IMG_SHAPE))
#всё объединяем
image_gen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, rotation_range=45, zoom_range=0.5, width_shift_range=0.15, height_shift_range=0.15)
train_data_gen = image_gen.flow_from_directory(batch_size=batch_size, directory=train_dir, shuffle=True, target_size=(IMG_SHAPE,IMG_SHAPE), class_mode='binary')

#создаём валидационный набор данных
image_gen_val = ImageDataGenerator(rescale=1./255)
val_data_gen = image_gen_val.flow_from_directory(batch_size=batch_size, directory=val_dir, target_size=(IMG_SHAPE,IMG_SHAPE), class_mode='binary')

#создаём модель
model = Sequential([
    Conv2D(16,(3,3), activation='relu', input_shape=(IMG_SHAPE,IMG_SHAPE,3)),
    MaxPooling2D(2,2),
    Conv2D(32,(3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(64,(3,3), activation='relu'),
    MaxPooling2D(2,2),
    Dropout(0.2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(5, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#обучение модели
epochs = 85
SPE = len(train_data_gen.classes) // batch_size
VS = len(val_data_gen.classes) // batch_size
model.fit(train_data_gen, validation_data=val_data_gen, epochs=epochs, steps_per_epoch=SPE, validation_steps=VS)
model.save('models/search_flowers.h5')

# # вывод графиков
# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']

# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs_range = range(epochs)

# plt.figure(figsize=(8,8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Точность на обучении')
# plt.plot(epochs_range, val_acc, label='Точность на валидации')
# plt.legend(loc='lower right')
# plt.title('Точность на обучающих и валидационных данных')

# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Потери на обучении')
# plt.plot(epochs_range, val_loss, label='Потери на валидации')
# plt.legend(loc='upper right')
# plt.title('Потери на обучающих и валидационных данных')
# plt.savefig('./foo3.png')
# plt.show()
#сделал 3 обучения и выявел, что лучше всего подходит 80-85 эпох, если делать без с расширением данных экспериментов, то -8 строк будет,
#остальное можно оставить, график для наглядности