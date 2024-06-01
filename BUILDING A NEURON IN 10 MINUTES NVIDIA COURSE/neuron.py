import tensorflow as tf
tf.config.list_physical_devices('GPU')
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (valid_images, valid_labels) = fashion_mnist.load_data()

import matplotlib.pyplot as plt
# 0- T-Shirt, 1-Trouser, 2-Pullover, 3-Dress, 4-Coat, 5-Sandal, 6-Shirt, 7-Sneaker, 8-Bag, 9-Ankle Boot
data_idx = 3

plt.figure()
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)
plt.show()

# Replace "number_of_classes" with the actual number of classes in the dataset
number_of_classes = 10

x_values = range(number_of_classes)

# Define the model variable
model = tf.keras.models.Sequential()

plt.figure()
plt.bar(x_values, model.predict(train_images[data_idx:data_idx+1]).flatten())
plt.xticks(range(10))
plt.show()

print("Correct Answer: ", train_labels[data_idx])


