# Implementing Softmax function

The softmax function, also known as softargmax[1]: 184  or normalized exponential function,[2]: 198  converts a vector of K real numbers into a probability distribution of K possible outcomes. It is a generalization of the logistic function to multiple dimensions, and used in multinomial logistic regression. The softmax function is often used as the last activation function of a neural network to normalize the output of a network to a probability distribution over predicted output classes, based on Luce's choice axiom. 


The softmax function takes as input a vector z of K real numbers, and normalizes it into a probability distribution consisting of K probabilities proportional to the exponentials of the input numbers. That is, prior to applying softmax, some vector components could be negative, or greater than one; and might not sum to 1; but after applying softmax, each component will be in the interval ( 0 , 1 ) (0,1), and the components will add up to 1, so that they can be interpreted as probabilities.

Softmax Formula

The softmax formula is as follows:

sigma(z) = e^z / sigma (j=1 to K) (e^z)

Mathematical definition of the softmax function