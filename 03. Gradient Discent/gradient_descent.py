import numpy as np

def gradient_descent(x, y):
  m = b = 0   
  iterations = 10
  n = len(x)
  learning_rate = 0.001

  for i in range(iterations):
    # Calculate the predicted y values using the current m and b
    y_predicted = m * x + b

    # Compute the cost (mean squared error)
    cost =  1/n * sum([val ** 2 for val in (y-y_predicted)])

    # Calculate the gradients fro m and b
    md = -(2/n) * sum(x*(y- y_predicted))
    bd = -(2/n) * sum(y-y_predicted)

    # Update m and b using the gradients and the learning rate
    m = m - learning_rate * md
    b = b - learning_rate * bd

    print("m {}, b {}, cost {}, iterations {}".format(m, b, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)