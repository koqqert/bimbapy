import os
import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt 
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Dense, Flatten, Dropout

def generator(dir, gen = ImageDataGenerator(rescale=1./255),shuffle=True,batch_size=1,target_size=(24,24),class_mode='categorical'):
    '''
    dir(str) - the directory
    gen(str) - генератор и нормализация данных
    shuffle(bool) - перемешивать ли данные
    batch_size(int) - размер батча
    target_size(tuple) - размер изображения
    class_mode(str) - режим работы с классами ('categorical')
    '''
    return gen.flow_from_directory(dir, target_size=target_size, shuffle=shuffle,color_mode='grayscale',batch_size=batch_size, class_mode=class_mode)

BS = 32 #batch_size
TS = (24,24) #target_size
train_batch = generator('data/train',shuffle=True, batch_size=BS,target_size=TS)
valid_batch = generator('data/test',shuffle=True,batch_size=BS,target_size=TS)
SPE = len(train_batch.classes) // BS
VS = len(valid_batch.classes) // BS

num_classes = len(train_batch.class_indices)

model = Sequential([
    #первый сверточный слой
    Conv2D(32, (3,3), activation='relu', input_shape=(24,24,1)),
    MaxPooling2D((2,2)),
    #второй сверточный слой
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    #третий сверточный слой
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    #случайным образом включайте и выключайте нейроны, чтобы улучшить конвергенцию
    Dropout(0.25),
    #flatten поскольку измерений слишком много, нам нужен только результат классификации
    Flatten(),
    #полносвязный слой
    Dense(128, activation='relu'),
    #ещё один dropout ради сближения :>
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#обучение модели
history = model.fit(train_batch, validation_data=valid_batch,epochs=15,steps_per_epoch=SPE,validation_steps=VS)
# model.save('models/opcl_eyes.h5')
#вывод графиков

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(15)

plt.figure(figsize=(8,8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Точность на обучении')
plt.plot(epochs_range, val_acc, label='Точность на валидации')
plt.legend(loc='lower right')
plt.title('Точность на обучающих и валидационных данных')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Потери на обучении')
plt.plot(epochs_range, val_loss, label='Потери на валидации')
plt.legend(loc='upper right')
plt.title('Потери на обучающих и валидационных данных')
plt.savefig('./foo.png')
plt.show()

