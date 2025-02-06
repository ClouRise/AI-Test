import numpy as np

def activate(n):
    return 0 if n < 0.5 else 1

def porksh(dop,mark,eps):
    if (dop > 10) or (mark > 100) or (eps > 100):
        print("ты обманул поркша")
        return -1
    if mark < 61: return -1

    dop /= 10
    mark /= 100
    eps /= 100
    
    x = np.array([dop,mark,eps])
    weightHidden1 = np.array([[0.5,0.5,0],[0,0,0.5]])
    weightHidden2 = np.array([1,-0.5])

    z = np.dot(weightHidden1,x)
    arr = np.array([activate(i) for i in z])
    z = np.dot(weightHidden2,arr)
    return(z)

dop = int(input('сколько допусков сдал(макс 10): '))
mark = int(input('сколько баллов набрал(макс 100): '))
eps = int(input('сколько пар пропустил(макс 100): '))
info = porksh(dop,mark,eps) 
if info >= 0.5: print("не отчислен")
else: print("отчислен")