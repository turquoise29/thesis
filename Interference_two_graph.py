import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

Dir = "G:\\My Drive\\Research\\M1\\data\\20230528_Interference"

def makeFig2():
    plt.figure(figsize=(8,5))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    for file in sorted(glob.glob(Dir + "/*.txt")):
        array = pd.read_table(file, header=None, skiprows=66, skipfooter=1, encoding="cp932", engine="python").values
        label = "no graphene" if os.path.splitext(os.path.basename(file))[0][0]=="k" else "suspended graphene"
        plt.plot(array[:, 0], array[:, 1], label=label)
    plt.xlim(400, 700)
    plt.xlabel("Wavelength (nm)", fontsize=24)
    plt.ylabel("Reflectance (%)", fontsize=24)
    plt.ylim(0, 50)
    plt.legend(frameon=False, fontsize=20)
    plt.tick_params(width=2, length=10, labelsize=24)
    plt.tight_layout()
    plt.savefig(os.path.join(Dir, "output.png"), bbox_inches='tight')
    plt.clf()

makeFig2()
