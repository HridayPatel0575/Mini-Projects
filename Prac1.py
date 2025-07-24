import numpy as np

x= [1,2,3,4,5]
y= [50,55,65,70,75]

x_m = np.mean(x)
y_m = np.mean(y)

n =int(len(x))

sum1 =0 
sum2 =0
for i in range(n):
    sum1=sum1+((x[i]-x_m)*(y[i]-y_m))

for i in range(n):
    sum2=sum2+((x[i]-x_m)*(x[i]-x_m))

    

b1= sum1/sum2

b0 = y_m - (b1*x_m)

print(b0)
