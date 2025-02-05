import numpy as np

def activate(n):
    return 0 if n < 0.5 else 1

def head(humid,temp,rain):
    x = np.array([humid,temp,rain])
    weightHide = np.array([1,1,1])
    weightEnd = np.array([-1,1])
    z = np.dot(weightHide,x)
    print (z)
    arr = np.array([activate(i) for i in z])
    print(arr)

    sum = np.dot(arr, weightEnd)
    end = activate(sum)

    print(end)

head() 