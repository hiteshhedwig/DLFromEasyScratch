# Implementing ChainRule

The chain rule is a mathematical theorem that lets us compute derivatives of composite functions and reasoning about their derivatives is essential to training them.

ChatGPT way of explaining :
```
The chain rule is like a recipe for making a cake. Imagine that you have a recipe for a cake that has multiple steps, and each step depends on the result of the previous step. For example, you might have to mix some ingredients together, then bake them in the oven, then add some frosting on top.

Now imagine that you want to make a different kind of cake, but you still want to use the same recipe. You'll need to figure out how to adjust the recipe to get the new cake. This is where the chain rule comes in.

The chain rule helps you figure out how to change each step of the recipe to get the new cake. It does this by showing you how much each step of the recipe contributes to the final result. You can use this information to adjust each step of the recipe to get the new cake.

In the same way, in deep learning, we use the chain rule to figure out how to adjust the weights and biases of a neural network to get better results. The neural network is like the recipe for the cake, and the weights and biases are like the ingredients. The chain rule tells us how much each weight and bias contributes to the final output of the neural network. We can use this information to adjust the weights and biases to get better results.
```

## Another by ChatGPT

Suppose we have a simple neural network with one input node, one hidden node, and one output node. The neural network looks like this:

rust

      w1
x ------> h ------> y

where x is the input, h is the hidden node, y is the output, and w1 is the weight connecting x to h.

The output y is calculated by applying an activation function g to the weighted sum of the input x and the weight w1:

y = g(w1 * x)

We want to train the neural network to predict the correct output y for a given input x. To do this, we need to adjust the weight w1 based on the error between the predicted output y and the true output y_true.

Let's say we have a loss function L that measures the error between y and y_true. To update the weight w1, we need to calculate the gradient of the loss function with respect to w1.

Using the chain rule, we can express the gradient of the loss function with respect to w1 in terms of the gradient of the loss function with respect to y, and the gradient of y with respect to w1:

dL/dw1 = (dL/dy) * (dy/dw1)

where:

    dL/dy is the derivative of the loss function with respect to y, which measures how much changing y will affect the loss.
    dy/dw1 is the derivative of y with respect to w1, which measures how much changing w1 will affect y.

To calculate these derivatives, we can use the following equations:

    dL/dy = (y - y_true) * g'(w1 * x)
    dy/dw1 = x * g'(w1 * x)

where g' is the derivative of the activation function g.

The first equation gives us the gradient of the loss function with respect to y. It tells us that the gradient depends on the difference between y and y_true, and the derivative of the activation function g evaluated at w1 * x.

The second equation gives us the gradient of y with respect to w1. It tells us that the gradient depends on the input x and the derivative of the activation function g evaluated at w1 * x.

Finally, we can plug these equations into the chain rule formula to get the gradient of the loss function with respect to w1:

dL/dw1 = (y - y_true) * g'(w1 * x) * x

This tells us how much changing w1 will affect the loss, based on the error between y and y_true, the derivative of the activation function g, and the input x.

We can use this gradient to update the weight w1 during training, by subtracting a small multiple of the gradient from the current weight.