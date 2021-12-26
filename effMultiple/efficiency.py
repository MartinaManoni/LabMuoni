# general. Not even sure we are actually using it

import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

def getfile(HV):
    mynp = np.loadtxt("coincM_HV"+str(HV)+".txt",unpack=False, skiprows=2)
    print ("high voltage is: ", HV)
    return mynp.T

# thing [row][column]
# thr, s, d, t
def efficiency (mynp):
    d = mynp[2]
    t = mynp[3]
    e = t/d
    err = np.sqrt((e*(1-e))/d)
    return e, err

mynp850 = getfile(850)
eff850, err850 = efficiency(mynp850)
print (mynp850[0])
print (eff850)
ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=1000V t=100s")
ax.plot(mynp850[0],eff850, "-",color = "royalblue", marker='.', alpha = 0.6, label="G1")
plt.errorbar(mynp850[0], eff850, yerr=err850, xerr=None)
#ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("eff")
plt.grid()

plt.show()



print (mynp850)





