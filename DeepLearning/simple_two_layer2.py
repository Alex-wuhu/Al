

import random
import math
import numpy as np 
m=100000    #train samples
n=1000    #test samples 
k=5000    #train times /iterations
theta=0.85   #learning rate
x_train=np.zeros((m,1))
y_train=np.zeros((m,1))
x_test=np.zeros((n,1))
y_test=np.zeros((n,1))
w1=np.random.normal(0,0.01,(1,1))
b1=np.zeros(1)
w2=np.random.normal(0,0.01,(1,1))
b2=np.zeros(1)
#initilze y_train
for i in range(m):
    degree_value=random.uniform(0,360)
    cosine_value=math.cos(math.radians(degree_value))
    x_train[i]=[degree_value]
    if cosine_value>0:
        y_train[i]=1
    else:
        y_train[i]=0
#initilze y_test
for i in range(n):
    degree_value2=random.uniform(0,360)
    cosine_value2=math.cos(math.radians(degree_value2))
    x_test[i]=[degree_value2]
    if cosine_value2>0:
        y_test[i]=1
    else:
        y_test[i]=0

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
def predict(x,w1,b1,w2,b2,number):
    y=sigmod((sigmod(np.dot(x,w1)+b1)*w2)+b2)
    for i in range(number):
        if y[i]>=0.5:
            y[i]=1
        else:
            y[i]=0
    return y


#train
for i in range(1,k+1):
    z1=np.dot(x_train,w1) + b1
    a1=sigmod(z1)
    z2=np.dot(a1,w2) + b2
    a2=sigmod(z2)
    dz2=np.subtract(a2,y_train)    #only for cross-entroy
    dw2=1/m*(np.dot(a1.T,dz2))
    db2=1/m*np.sum(dz2)
    dz1=np.dot(dz2,w2.T)*(a1*(1-a1))
    dw1=1/m*(np.dot(x_train.T,dz1))
    db1=1/m*np.sum(dz1)
    w1=w1-theta*dw1
    b1=b1-theta*db1
    w2=w2-theta*dw2
    b2=b2-theta*db2
    #if(i%500==0):
    #    print(f"{i} iterations :\n w1 = {w1}, b1={b1}, w2={w2}, b2={b2}")

print(w1)
print(b1)
print(w2)
print(b2)
#predict 
y_pred=predict(x_train,w1,b1,w2,b2,m)
y_pred_test=predict(x_test,w1,b1,w2,b2,n)
#train_accurcy
def accurcy(y_pred,y,number):
    return np.count_nonzero(y_pred==y)/number
print(f"cost on train set: {cost_func(y_pred,y_train,m)}")
print(f"cost on test set: {cost_func(y_pred_test,y_test,n)}")
print(f"accurcy on train set: {accurcy(y_pred,y_train,m)}")
print(f"accurcy on test set: {accurcy(y_pred_test,y_test,n)}")
