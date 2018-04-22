# https://www.tensorflow.org/programmers_guide/eager

from __future__ import absolute_import, division, print_function

import tensorflow as tf

tf.enable_eager_execution()

tf.executing_eagerly()        # => True

x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))  # => "hello, [[4.]]"



a = tf.constant([[1, 2],
                 [3, 4]])
print(a)
# => tf.Tensor([[1 2]
#               [3 4]], shape=(2, 2), dtype=int32)

# Broadcasting support
b = tf.add(a, 1)
print(b)
# => tf.Tensor([[2 3]
#               [4 5]], shape=(2, 2), dtype=int32)

# Operator overloading is supported
print(a * b)
# => tf.Tensor([[ 2  6]
#               [12 20]], shape=(2, 2), dtype=int32)

# Use NumPy values
import numpy as np

c = np.multiply(a, b)
print(c)
# => [[ 2  6]
#     [12 20]]

# Obtain numpy value from a tensor:
print(a.numpy())
# => [[1 2]
#     [3 4]]


import tensorflow.contrib.eager as tfe

w = tfe.Variable([[1.0]])
with tfe.GradientTape() as tape:
  loss = w * w

grad = tape.gradient(loss, [w])
print(grad)  # => [tf.Tensor([[ 2.]], shape=(1, 1), dtype=float32)]