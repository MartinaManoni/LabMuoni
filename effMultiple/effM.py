import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

def getfile(HV):
    mynp = np.loadtxt("coincM_HV"+str(HV)+".txt",unpack=False, skiprows=4)
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

mynp950 = getfile(950)
eff950, err950 = efficiency(mynp950)
mynp1000 = getfile(1000)
eff1000, err1000 = efficiency(mynp1000)

'''
ax = plt.figure(figsize=(7,5), dpi=100,facecolor="w").add_subplot(111)
plt.suptitle("Scintillator responses HV=1000V t=100s")
ax.plot(mynp950[0],eff950, "-",color = "royalblue", marker='.', alpha = 0.6, label="G1")
plt.errorbar(mynp950[0], eff950, yerr=err950, xerr=None)
#ax.set_yscale("log")
plt.legend()
plt.xlabel("thr")
plt.ylabel("eff")
plt.grid()

plt.show()

'''

#print (mynp950)
print ("\n\nooooooooooooooooooooooooooooooooooooooooooooooooooooo\n")
print ("Efficiency:")

print ("\n HV 950V")
for i in range(np.size(eff950)):
    print ("thr: ", round(mynp950[0][i],3), " eff: ", round(eff950[i],3), " +- ", round(err950[i],3))

print("\n HV 1000V")
for i in range(np.size(eff1000)):
    print ("thr: ", round(mynp1000[0][i],3), " eff: ", round(eff1000[i],3), " +- ", round(err1000[i],3))

x = [950, 1000]
x = np.asarray(x)

ax = plt.axis[0, 0]
c = ax.pcolor(950, round(mynp950[0,:],3) , round(eff950[:],3), cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolor')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)


plt.show()

