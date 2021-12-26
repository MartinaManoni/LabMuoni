import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

def getfile(HV):
    thr, s, t = np.loadtxt("STminerva_HV"+str(HV)+".txt",unpack=True, skiprows=4)
    stdS = np.sqrt(s)/100
    stdT = np.sqrt(t)/100
    s = s/100
    t = t/100
    return thr, s, t, stdS, stdT

# RATES
thr950, s950, t950, errs950, errt950 = getfile(950)
thr1000, s1000, t1000, errs1000, errt1000 = getfile(1000)
thr1050, s1050, t1050, errs1050, errt1050 = getfile(1050)
maxrange = np.amax(t950) +3

ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Minerva's response t=100s")
plt.errorbar(thr950, t950, yerr=errt950, xerr=None, color ='gold', label="HV=950V, triple")
plt.errorbar(thr950, s950, yerr=errs950, xerr=None, color ='orange', label="HV=950V, single")
plt.errorbar(thr1050, t1050, yerr=errt1050, xerr=None, color ='cornflowerblue', label="HV=1050V, triple")
plt.errorbar(thr1050, s1050, yerr=errs1050, xerr=None, color ='royalblue', label="HV=1050V, single")
plt.errorbar(thr1000, t1000, yerr=errt1000, xerr=None, color ='green', label="HV=1000V, triple")
plt.errorbar(thr1000, s1000, yerr=errs1000, xerr=None, color ='green', label="HV=1000V, single")
#ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("rate")
plt.ylim((0,maxrange))
plt.grid()

plt.show()
