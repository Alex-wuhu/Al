import random
import math
import numpy as np 
m=10    #train samples
n=1000    #test samples 
k=5000    #train times /iterations
theta=0.8   #learning rate
x_train=np.zeros((m,1))
y_train=np.zeros((m,1))
x_test=np.zeros((n,1))
y_test=np.zeros((n,1))
w=np.random.normal(0,0.01,(1,1))
b=np.zeros(1)
#initilze y_train
for i in range(m):
    degree_value=random.uniform(0,360)
    sine_value=math.sin(math.radians(degree_value))
    x_train[i]=[degree_value]
    if sine_value>0:
        y_train[i]=1
    else:
        y_train[i]=0
#initilze y_test
for i in range(n):
    degree_value2=random.uniform(0,360)
    sine_value2=math.sin(math.radians(degree_value2))
    x_test[i]=[degree_value2]
    if sine_value2>0:
        y_test[i]=1
    else:
        y_test[i]=0

def Relu(x):
    return np.maximum(0,x)
def sigmod(x):
    return 1/(1+np.exp(-x))
def cost_func(y_temp,y,m):
    y_pred=np.copy(y_temp)
    for i in range (m):
        if y_pred[i]==1 :
            y_pred[i]=1-1e-6
        elif y_pred[i]==0:
            y_pred[i]=1e-6    
    
    arr=-(y*np.log(y_pred)+(1-y)*np.log(1-y_pred))
    return arr.mean()
def predict(x,w,b,number):
    y=sigmod(np.dot(x,w)+b)
    for i in range(number):
        if y[i]>0.5:
            y[i]=1
        else:
            y[i]=0
    return y
#train
for i in range(1,k+1):
    z=np.dot(x_train,w) + b
    a=sigmod(z)
    dz=np.subtract(a,y_train)    #only for cross-entroy
    dw=1/m*(np.dot(x_train.T,dz))
    db=1/m*np.sum(dz)
    w=w-theta*dw
    b=b-theta*db
    if(i%500==0):
        print(f"{i} iterations :\n w = {w}, b={b}")
#predict 
y_pred=predict(x_train,w,b,m)
y_pred_test=predict(x_test,w,b,n)
#train_accurcy
def accurcy(y_pred,y,number):
    return np.count_nonzero(y_pred==y)/number
#print(f"cost on train set: {cost_func(y_pred,y_train,m)}")
#print(f"cost on test set: {cost_func(y_pred_test,y_test,n)}")
print(f"accurcy on train set: {accurcy(y_pred,y_train,m)}")
print(f"accurcy on test set: {accurcy(y_pred_test,y_test,n)}")
