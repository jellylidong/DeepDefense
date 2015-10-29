
# coding: utf-8

# In[1]:

from __future__ import absolute_import
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import Convolution1D, MaxPooling1D



# In[84]:

def transIP(ip):
    tmp = ip.split(".")
    res = ""
    for str in tmp:
        if len(str) == 1:
            str = "00" + str
        else :
            if len(str) == 2:
                str = "0" + str
        res += str
    return int(res)/1000000


# In[89]:

# set parameters:
max_features = 900000
maxlen = 4
batch_size = 32
embedding_dims = 100
nb_filter = 250
filter_length = 3
hidden_dims = 250
nb_epoch = 3



# In[90]:

import numpy as np

x_train = []
y_train = []
x_test  = []
y_test  = []

counter = 0;
data = open("csv/output.csv", "r")
for line in data:
    tmp = line.split(',')
    #print(tmp[0])
    tmp[0] = int(float(tmp[0]) * 100)
    #print(tmp[0])
    tmp[1] = transIP(tmp[1])
    tmp[2] = transIP(tmp[2])
    x_train.append(tmp[0:3])
    y_train.append(1)
    counter += 1
    if(counter > 500):break
counter = 0
for line in data:
    tmp = line.split(',')
    tmp[0] = int(float(tmp[0]) * 100)
    tmp[1] = transIP(tmp[1])
    tmp[2] = transIP(tmp[2])
    x_test.append(tmp[0:3])
    y_test.append(1)
    counter += 1
    if(counter > 100):break
        
        
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print(x_train[1])

print("Pad sequences (samples x time)")
X_train = sequence.pad_sequences(x_train, maxlen=maxlen)
X_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)


# In[91]:

print(X_train[1])


# In[92]:

print('Build model...')
model = Sequential()

# we start off with an efficient embedding layer which maps
# our vocab indices into embedding_dims dimensions
model.add(Embedding(max_features, embedding_dims, input_length=maxlen))
model.add(Dropout(0.25))

# we add a Convolution1D, which will learn nb_filter
# word group filters of size filter_length:
model.add(Convolution1D(nb_filter=nb_filter,
                        filter_length=filter_length,
                        border_mode="valid",
                        activation="relu",
                        subsample_length=1))
# we use standard max pooling (halving the output of the previous layer):
model.add(MaxPooling1D(pool_length=2))

# We flatten the output of the conv layer, so that we can add a vanilla dense layer:
model.add(Flatten())

# We add a vanilla hidden layer:
model.add(Dense(hidden_dims))
model.add(Dropout(0.25))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', class_mode="binary")
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch, show_accuracy=True, validation_data=(X_test, y_test))

