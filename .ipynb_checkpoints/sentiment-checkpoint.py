import tensorflow as tf 

# print(tf.__version__)


import tensorflow_datasets as tfds 

imdb,info = tfds.load('imdb_reviews',with_info=True,as_supervised=True)
