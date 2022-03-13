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

class amadeus():
    def __init__(self, path, image_size, batch_size):
        self.image_size = image_size
        self.batch_size = batch_size

        self.dataset_training, self.dataset_validation = self.load_datasets(path)
        self.model = self.construct_model()

    def load_datasets(self, path):
        dataset_training = keras.preprocessing.image_dataset_from_directory(
            path, 
            validation_split=0.2,
            seed=1337,
            subset="training",
            image_size=self.image_size,
            labels="inferred",
            batch_size=self.batch_size,
        )

        dataset_validation = keras.preprocessing.image_dataset_from_directory(
            path,
            validation_split=0.2,
            seed=1337,
            subset="validation",
            image_size=self.image_size, 
            labels="inferred", 
            batch_size=self.batch_size,
        )
        return (dataset_training, dataset_validation)
    
    def construct_model(self):
        inputs = keras.Input(shape=self.image_size+(3,))
        x = layers.Rescaling(scale=1.0/255)(inputs)

        x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)
        x = layers.MaxPooling2D(pool_size=(3, 3), padding="same")(x)
        x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)
        x = layers.MaxPooling2D(pool_size=(3, 3), padding="same")(x)
        x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same")(x)

        x = layers.GlobalAveragePooling2D()(x)

        num_classes = 16
        outputs = layers.Dense(num_classes, activation="softmax")(x)

        return keras.Model(inputs=inputs, outputs=outputs)
    
    def fit(self, epochs):
        callbacks = [
            keras.callbacks.ModelCheckpoint("./saves/save_at_{epoch}.h5"),
        ]
        self.model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
        self.model.fit(self.dataset_training, epochs=epochs, callbacks=callbacks, validation_data=self.dataset_validation)

    def test_accuracy_on_image(self, path):
        img = keras.preprocessing.image.load_img(path, target_size=self.image_size)
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = self.model.predict(img_array)
        score = predictions[0]

        print(f"this shits probably a(n) {vocab[np.argmax(score)]} idk man")