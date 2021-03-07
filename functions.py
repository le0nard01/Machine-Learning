import matplotlib.pyplot as plt
import math
import numpy as np

#numbers = np.random.randn(500)
numbers = np.arange(-10, 10, 0.05)


#Activation Functions:
#Step function y = 1 {x>0} | y = 0 {x<=0}
def Step_Function(x):
    return 1 if x>0 else 0

def Linear_Function(x):
    return x

def Sigmoid_Function(x):
    return 1/(1+(math.e**-x))

def ReLU_Function(x): #Rectified_Linear_Function
    return x if x>0 else 0

y = [ReLU_Function(A) for A in numbers]
z = list(zip(*sorted(zip(numbers,y))))

plt.plot(z[0],z[1])
plt.show()