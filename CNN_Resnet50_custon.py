import time
import random
import tensorflow as tf
from tensorflow import keras
from keras.models import Model, load_model
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from keras.applications.resnet import ResNet50
from keras_preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np


def resnet50_Binaria():
  train_dataset = "../classf_binaria/train"
  test_dataset = "../classf_binaria/test"
  val_dataset = "../classf_binaria/val"

  height, width = (224, 224)
  epochs_no = 15
  classes_name = ('0','1')
  batch_size = 34

  f = open("saidas.txt", 'w')

  imgdatagen = ImageDataGenerator(rescale=1 / 255.0,
          rotation_range=20,
          zoom_range=0.05,
          width_shift_range=0.05,
          height_shift_range=0.05,
          shear_range=0.05,
          horizontal_flip=True,
          fill_mode="nearest",
          validation_split=0.20
  )

  train_pre_dataset = imgdatagen .flow_from_directory(train_dataset, target_size = (height, width), 
                classes = classes_name,  batch_size = batch_size)

  test_pre_dataset = imgdatagen .flow_from_directory(test_dataset, target_size = (height, width), 
                classes = classes_name, batch_size = batch_size)

  val_pre_dataset = imgdatagen .flow_from_directory(val_dataset, target_size = (height, width), 
                classes = classes_name, batch_size = batch_size, shuffle = False)

  ResNet_model = load_model('../resultados_rede/Binaria-56pp_2exResNet_model.h5')
  '''
  base_model= ResNet50(include_top=False, weights="imagenet", input_shape=(height, width,3))
  ResNet_model= Sequential()
  ResNet_model.add(base_model)
  ResNet_model.add(Conv2D(64, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(64, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(128, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(128, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(MaxPooling2D(pool_size = (2, 2)))
  ResNet_model.add(Conv2D(256, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(256, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(MaxPooling2D(pool_size = (2, 2)))
  ResNet_model.add(Flatten())
  ResNet_model.add(Dense(4096,activation='relu'))
  ResNet_model.add(Dense(2048,activation='relu'))
  ResNet_model.add(Dense(512,activation='relu'))
  ResNet_model.add(Dense(2, activation='sigmoid'))
  ResNet_model.summary()
  
  start_time = time.time()

  learn_control = ReduceLROnPlateau(monitor='val_accuracy', patience=3, verbose=1, factor=.5, min_lr=0.0001)

  ResNet_history = ResNet_model.fit(train_pre_dataset,
                              steps_per_epoch=train_pre_dataset.samples//train_pre_dataset.batch_size,
                              validation_data=val_pre_dataset,
                              verbose=1,
                              validation_steps=val_pre_dataset.samples//val_pre_dataset.batch_size,
                              epochs=epochs_no,callbacks=[learn_control])

  ResNet_model.save('../resultados_rede/Binario-ResNet_model.h5')

  print("---  %d:%.2d minutes ---" % divmod(time.time() - start_time, 60))
  '''
  test_set = test_pre_dataset
  test_set.reset()
  predictions = ResNet_model.predict(test_pre_dataset)
  y_pred = np.argmax(predictions, axis=-1)

  y_test = test_pre_dataset.labels
  cm = confusion_matrix(y_test,y_pred)

  print(cm, file=f)

  print(classification_report(test_pre_dataset.classes, y_pred,zero_division=0), file=f)

  print(f'Result ResNet50_custon\n: {predictions}', file=f)

  f.close()

def resnet50_5classesKL():
  train_dataset = "../classf_5_classes_KL/train"
  test_dataset = "../classf_5_classes_KL/test"
  val_dataset = "../classf_5_classes_KL/val"

  height, width = (224, 224)
  epochs_no = 30
  classes_name = ('0','1','2','3','4')
  batch_size = 34

  f = open("saidas.txt", 'w')

  imgdatagen = ImageDataGenerator(rescale=1 / 255.0,
          rotation_range=20,
          zoom_range=0.05,
          width_shift_range=0.05,
          height_shift_range=0.05,
          shear_range=0.05,
          horizontal_flip=True,
          fill_mode="nearest",
          validation_split=0.20
  )

  train_pre_dataset = imgdatagen .flow_from_directory(train_dataset, target_size = (height, width), 
                classes = classes_name,  batch_size = batch_size)

  test_pre_dataset = imgdatagen .flow_from_directory(test_dataset, target_size = (height, width), 
                classes = classes_name, batch_size = batch_size)

  val_pre_dataset = imgdatagen .flow_from_directory(val_dataset, target_size = (height, width), 
                classes = classes_name, batch_size = batch_size, shuffle = False)

  ResNet_model = load_model('../resultados_rede/ResNet_model-30pp-2ex.h5')
  '''
  base_model= ResNet50(include_top=False, weights="imagenet", input_shape=(height, width,3))
  ResNet_model= Sequential()
  ResNet_model.add(base_model)
  ResNet_model.add(Conv2D(64, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(64, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(128, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(128, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(MaxPooling2D(pool_size = (2, 2)))
  ResNet_model.add(Conv2D(256, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(Conv2D(256, (3, 3), padding='same', activation = 'relu'))
  ResNet_model.add(MaxPooling2D(pool_size = (2, 2)))
  ResNet_model.add(Flatten())
  ResNet_model.add(Dense(4096,activation='relu'))
  ResNet_model.add(Dense(2048,activation='relu'))
  ResNet_model.add(Dense(512,activation='relu'))
  ResNet_model.add(Dense(5, activation='softmax'))
  ResNet_model.summary()
  
  for layer in ResNet_model.layers[-10:]:
    layer.trainable = False

  ResNet_model.summary()

  ResNet_model.compile(optimizer=optimizers.Adam(learning_rate=0.001),loss="categorical_crossentropy",metrics=["accuracy"])

  
  start_time = time.time()

  learn_control = ReduceLROnPlateau(monitor='val_accuracy', patience=3, verbose=1, factor=.5, min_lr=0.0001)

  ResNet_history = ResNet_model.fit(train_pre_dataset,
                              steps_per_epoch=train_pre_dataset.samples//train_pre_dataset.batch_size,
                              validation_data=val_pre_dataset,
                              verbose=1,
                              validation_steps=val_pre_dataset.samples//val_pre_dataset.batch_size,
                              epochs=epochs_no,callbacks=[learn_control])

  ResNet_model.save('/content/drive/MyDrive/data/model - ResNet_model.h5')

  print("---  %d:%.2d minutes ---" % divmod(time.time() - start_time, 60))
  '''
  test_set = test_pre_dataset
  test_set.reset()
  predictions = ResNet_model.predict(test_pre_dataset)
  y_pred = np.argmax(predictions, axis=-1)

  y_test = test_pre_dataset.labels
  cm = confusion_matrix(y_test,y_pred)

  print(cm, file=f)

  print(classification_report(test_pre_dataset.classes, y_pred), file=f)

  print(f'Result ResNet50_custon:\n {predictions}', file=f)

  f.close()

'''
if __name__=='__main__':
  resnet50_Binaria()
  resnet50_5classesKL()
'''