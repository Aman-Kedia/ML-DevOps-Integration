from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

# load dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Flattening and Scaling the data
pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(-1 , pixels).astype('float32')/255
X_test = X_test.reshape(-1 , pixels).astype('float32')/255

# Conerting to Categorical Data
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Creating Model
model = Sequential()
model.add(Dense(units=512, input_dim=pixels, activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=10, activation='softmax'))


model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, verbose=2, validation_data=(X_test, y_test))

scores = model.evaluate(X_test, y_test)
print("Accuracy:  %.2f%%" % (scores[1]*100))

model.save("cnn/mnist_model.h5")

file1 = open("cnn/accuracy.txt","w").write(str(scores[1]*100))