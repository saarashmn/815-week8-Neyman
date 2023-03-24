import numpy as np
from numpy import c_
import matplotlib.pyplot as plt
import random
# My function:
def Gauss(numbs,mu_true, sigma):
    return 1./(np.sqrt(2.*np.pi)*sigma)*np.exp(-np.power((numbs - mu_true)/sigma, 2.)/2)
Nmeas = 100
Nexp  = 10000
bounds = 100

mu_experiment = 0

mu_true = 0
mu_best = 0
sigma = 1

#2D histogram 
X_Mu_True = [] #We will combines the two into a 2d plot using mathplot lib his2d
Y_Mu_Best = []  

# 3Neyman construction being implemented
for i in range(-bounds,bounds,1):
    mu_true = float(i)/10.
    
    for e in range (0,Nmeas):
        mu_best = 0
        for p in range(0,Nmeas):
            rando = random.random()
            x = Gauss(rando, mu_true, sigma)
            mu_best += x
        
        # our "measurement" for mu best fit
        mu_best = mu_best / float(Nmeas);
        Y_Mu_Best.append(mu_best)
        X_Mu_True.append(mu_true)
        
print(len(X_Mu_True))
print(len(Y_Mu_Best))
2000
2000
x_min = np.min(X_Mu_True)
x_max = np.max(X_Mu_True)

y_min = np.min(Y_Mu_Best)
y_max = np.max(Y_Mu_Best)

x_bins = np.linspace(x_min,x_max,70)
y_bins = np.linspace(y_min,y_max,70)

plt.title("Searching for the True alpha ")
plt.xlabel('$\mu$_True')
plt.ylabel('$\mu$_Best')
plt.hist2d(X_Mu_True,Y_Mu_Best, bins=[x_bins,y_bins], cmap=plt.cm.jet)
plt.colorbar()
plt.show()
