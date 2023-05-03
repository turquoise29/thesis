import numpy as np
import matplotlib.pyplot as plt

D2 = 0.007
D3 = 0.977
D4 = 0.35
D5 = 0.65

wave_lengths = np.arange(450, 651)

reflectances = []
for wave_length in wave_lengths:
    A7 = wave_length
    n = np.sqrt(D2*D4)*(1-2*(np.sqrt(D2*D4)+np.sqrt(D3*D5))*np.cos(4*np.pi()*D6/A7)+(np.sqrt(D2*D4)+np.sqrt(D3*D5))*(np.sqrt(D2*D4)+np.sqrt(D3*D5)))/(1+(D2*D4)-2*np.sqrt(D2*D4)*np.cos(4*np.pi()*D6/A7))*100
    reflectances.append(n)

plt.plot(wave_lengths, reflectances)
plt.xlim(450, 650)
plt.xticks(np.arange(450, 651, step=10))
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance (%)")

outDir = "G:\\My Drive\\Research\\Process\\Interference_simulation"
plt.savefig(outDir + "\\reflectance.png")