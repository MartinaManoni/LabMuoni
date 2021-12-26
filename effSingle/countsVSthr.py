import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

#### did this commit appear github?
######### GIOVE ############

x850, y850 = np.loadtxt("countsVSthr_G1_850V.txt",unpack=True, skiprows=2)
erry850 = np.sqrt(y850)/100.
y850 = y850/100.

x900, y900 = np.loadtxt("countsVSthr_G1_900V.txt",unpack=True, skiprows=2)
erry900 = np.sqrt(y900)/100.
y900 = y900/100.

x950, y950 = np.loadtxt("countsVSthr_G1_950V.txt",unpack=True, skiprows=2)
erry950 = np.sqrt(y950)/100.
y950 = y950/100.

x1000, y1000 = np.loadtxt("countsVSthr_G1_1000V.txt",unpack=True, skiprows=2)
erry1000 = np.sqrt(y1000)/100.
y1000 = y1000/100.

ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator response (Giove) t=100s")
ax.plot(x850,y850, "-",color = "dodgerblue", marker='.', alpha = 0.6, label="HV=850V")
ax.plot(x900,y900, "-",color = "blue", marker='.', alpha = 0.6, label="HV=900V")
ax.plot(x950,y950, "-",color = "orange", marker='.', alpha = 0.6, label="HV=950V")
ax.plot(x1000,y1000, "-",color = "crimson", marker='.', alpha = 0.6, label="HV=1000V")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()

######### GIUNONE ############
xx850, yy850 = np.loadtxt("countsVSthr_G2_850V.txt",unpack=True, skiprows=2)
erryy850 = np.sqrt(yy850)/100.
yy850 = yy850/100.

xx900, yy900 = np.loadtxt("countsVSthr_G2_900V.txt",unpack=True, skiprows=2)
erryy900 = np.sqrt(yy900)/100.
yy900 = yy900/100.

xx950, yy950 = np.loadtxt("countsVSthr_G2_950V.txt",unpack=True, skiprows=2)
erryy950 = np.sqrt(yy950)/100.
yy950 = yy950/100.


xx1000, yy1000 = np.loadtxt("countsVSthr_G2_1000V.txt",unpack=True, skiprows=2)
erryy1000 = np.sqrt(yy1000)/100.
yy1000 = yy1000/100.

ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator response (Giunone G2) t=100s")
ax.plot(xx850,yy850, "-",color = "dodgerblue", marker='.', alpha = 0.6, label="HV=850V")
ax.plot(xx900,yy900, "-",color = "blue", marker='.', alpha = 0.6, label="HV=900V")
ax.plot(xx950,yy950, "-",color = "orange", marker='.', alpha = 0.6, label="HV=950V")
ax.plot(xx1000,yy1000, "-",color = "crimson", marker='.', alpha = 0.6, label="HV=1000V")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()


######### MINERVA ############
xxx850, yyy850 = np.loadtxt("countsVSthr_M_850V.txt",unpack=True, skiprows=2)
erryyy850 = np.sqrt(yyy850)/100.
yyy850 = yyy850/100.

xxx900, yyy900 = np.loadtxt("countsVSthr_M_900V.txt",unpack=True, skiprows=2)
erryyy900 = np.sqrt(yyy900)/100.
yyy900 = yyy900/100.

xxx950, yyy950 = np.loadtxt("countsVSthr_M_950V.txt",unpack=True, skiprows=2)
erryyy950 = np.sqrt(yyy950)/100.
yyy950 = yyy950/100.

xxx1000, yyy1000 = np.loadtxt("countsVSthr_M_1000V.txt",unpack=True, skiprows=2)
erryyy1000 = np.sqrt(yyy1000)/100.
yyy1000 = yyy1000/100.

ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator response (Minerva M) t=100s")
ax.plot(xxx850,yyy850, "-",color = "dodgerblue", marker='.', alpha = 0.6, label="HV=850V")
ax.plot(xxx900,yyy900, "-",color = "blue", marker='.', alpha = 0.6, label="HV=900V")
ax.plot(xxx950,yyy950, "-",color = "orange", marker='.', alpha = 0.6, label="HV=950V")
ax.plot(xxx1000,yyy1000, "-",color = "crimson", marker='.', alpha = 0.6, label="HV=1000V")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()



ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=900V t=100s")
ax.plot(x900,y900, "-",color = "royalblue", marker='.', alpha = 0.6, label="G1")
ax.plot(xx900,yy900, "-",color = "magenta", marker='.', alpha = 0.6, label="G2")
ax.plot(xxx900,yyy900, "-",color = "gold", marker='.', alpha = 0.6, label="M")
#ax.plot(xxx900,yyy900, "-",color = "blue", marker='.', alpha = 0.6, label="HV=900V")
#ax.plot(xxx950,yyy950, "-",color = "orange", marker='.', alpha = 0.6, label="HV=950V")
#ax.plot(xxx1000,yyy1000, "-",color = "crimson", marker='.', alpha = 0.6, label="HV=1000V")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()

ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=850V t=100s")
ax.plot(x850,y850, "-",color = "royalblue", marker='.', alpha = 0.6, label="G1")
ax.plot(xx850,yy850, "-",color = "magenta", marker='.', alpha = 0.6, label="G2")
ax.plot(xxx850,yyy850, "-",color = "gold", marker='.', alpha = 0.6, label="M")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()


######à TEST FIT ########

import scipy.optimize as opt
def func(x, a, b, c, d, e):
     #return a/(1+np.exp(-b*x+c))
     return d*np.power(x,3) + c*np.power(x,2) + b*x + a + e*np.power(x,4)
     
guess = [-1.00963483e-02, 9.82926822e-01, -4.57599008e+01, 8.47864677e+02, 4.96026377e-05, -9.37689782e-08]

guess = np.array(guess)
guess = 0.0001*guess
 
ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=950V t=100s")
ax.plot(x950,y950,color = "royalblue", marker='.', alpha = 0.6, label="G1")
ax.plot(xx950,yy950, "-",color = "magenta", marker='.', alpha = 0.6, label="G2")
ax.plot(xxx950,yyy950, "-",color = "gold", marker='.', alpha = 0.6, label="M")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()
popt_pol = np.polyfit(x950,y950,4)
popt, pcov = opt.curve_fit(func, x950, y950)#, p0=guess)
#plt.plot(x950, func(x950, *popt), label="fit")
#plt.plot(x950, func(x950, *popt_pol), label="fit")
print (popt)
print (popt_pol)


ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=1000V t=100s")
ax.plot(x1000,y1000, "-",color = "royalblue", marker='.', alpha = 0.6, label="G1")
ax.plot(xx1000,yy1000, "-",color = "magenta", marker='.', alpha = 0.6, label="G2")
ax.plot(xxx1000,yyy1000, "-",color = "gold", marker='.', alpha = 0.6, label="M")
#plt.errorbar(x1000, y1000, yerr=erry1000, xerr=None)
ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.grid()

plt.show()

#print (x900, y900)
#print (y)
