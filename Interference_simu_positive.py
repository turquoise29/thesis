import numpy as np
import matplotlib.pyplot as plt

outDir = "G:\\My Drive\\Research\\Process\\Interference_simulation_Graphene_on_Si"

D2 = 1.52
D3 = 1.00
D4 = 0.01
D5 = 1.00
wavelengths = np.arange(450, 651)

for depth in range(800, 2101, 10):
    D6 = depth
    reflectances = [] 
    for wavelength in wavelengths:
        A7 = wavelength
        n = np.sqrt(D2*D4)*(1-2*(np.sqrt(D2*D4)+np.sqrt(D3*D5))*np.cos(4*np.pi*D6/A7)+(np.sqrt(D2*D4)+np.sqrt(D3*D5))*(np.sqrt(D2*D4)+np.sqrt(D3*D5)))/(1+(D2*D4)-2*np.sqrt(D2*D4)*np.cos(4*np.pi*D6/A7))*100
        reflectances.append(n)
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(wavelengths, reflectances)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Reflectance (%)")
    ax.set_title(f"Depth: {depth} nm")
    ax.set_xticks(np.arange(450, 651, 10))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_position(("axes", -0.02))
    ax.spines["left"].set_position(("axes", -0.02))
    ax.tick_params(axis="both", direction="in", length=6, width=1)
    ax.tick_params(axis="x", labelsize=10)
    ax.grid(axis="x", color="grey", linestyle=":", linewidth=0.5)
    plt.savefig(f"{outDir}\\depth_{depth}(nm).png")
    plt.close()