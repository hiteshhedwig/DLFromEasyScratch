# Implementing LeakyReLU function

Leaky Rectified Linear Unit, or Leaky ReLU, is a type of activation function based on a ReLU, but it has a small slope for negative values instead of a flat slope. The slope coefficient is determined before training, i.e. it is not learnt during training. This type of activation function is popular in tasks where we may suffer from sparse gradients, for example training generative adversarial networks.


Relu is:

if x >= 0 then ;
    y=x
else :
    y=0


LeakyRelu is:

if x >= 0 then ;
    y=x
else :
    y=0.01x

