# Implementing NestedFunctions 

Basic example of nested functions is shown below:

x -> F1 -> F2 -> y

```
F2(F1(x))
```

Try reading it from inside out. Like, First perform `F1` function on `x` then `F2` function on the output of previous function.

Understanding this chaining is important to know chain rule that is implemented in DL. 