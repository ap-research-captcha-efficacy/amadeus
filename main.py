# ./samples should first be loaded by running sample_synthesizer.py

from amadeus import amadeus

a = amadeus("./samples", (12, 19), 32)
a.fit(20)
a.test_accuracy_on_image("./samples/e/4.png")
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

vocab = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

dataset_training = keras.preprocessing.image_dataset_from_directory(
    "./samples", 
    validation_split=0.2,
    seed=1337,
    subset="training",
    image_size=(12,19),
    labels="inferred",
    batch_size=32,
)

dataset_validation = keras.preprocessing.image_dataset_from_directory(
    "./samples",
    validation_split=0.2,
    seed=1337,
    subset="validation",
    image_size=(12,19), 
    labels="inferred", 
    batch_size=32,
)

inputs = keras.Input(shape=(12, 19, 3))
x = layers.Rescaling(scale=1.0/255)(inputs)

x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)
x = layers.MaxPooling2D(pool_size=(3, 3), padding="same")(x)
x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)
x = layers.MaxPooling2D(pool_size=(3, 3), padding="same")(x)
x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)

x = layers.GlobalAveragePooling2D()(x)

num_classes = 16
outputs = layers.Dense(num_classes, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)
# model.summary()
epochs = 15

callbacks = [
    keras.callbacks.ModelCheckpoint("./saves/save_at_{epoch}.h5"),
]
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
model.fit(
    dataset_training, epochs=epochs, callbacks=callbacks, validation_data=dataset_validation,
)
res = model.evaluate(dataset_validation, return_dict=True)
print(res)

img = keras.preprocessing.image.load_img(
    "./samples/e/31.png", target_size=(12,19)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = predictions[0]

print(f"this shits probably a(n) {vocab[np.argmax(score)]} idk man")
"""