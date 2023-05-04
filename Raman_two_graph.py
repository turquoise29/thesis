import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

Dir = "G:\\My Drive\\Research\\M1\\data\\20230427_Raman_sensor"

def makeFig2():
    files = sorted(glob.glob(f"{Dir}/*.csv"))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    xlims = [(1500,2800), (2625,2700), (1550,1600)]
    for i in range(3):
        fig, ax = plt.subplots(figsize=(8,5))
        for file in files:
            array = pd.read_csv(file, header=None, skiprows=19, skipfooter=47, encoding="shift-jis", engine='python').values
            fileName = os.path.splitext(os.path.basename(file))[0]
            label = "no strain" if fileName[0] == "s" else "strain management"
            kikaku = (array[:, 1] - min(array[:, 1])) / (max(array[:, 1]) - min(array[:, 1]))
            plt.plot(array[:, 0], kikaku, label=label, color='b' if fileName[0] == "k" else 'r')
        plt.xlim(xlims[i])
        plt.xlabel("Raman shift (cm$^{-1}$)", fontsize=24)
        plt.ylabel("Intensity (a.u.)", fontsize=24)
        plt.legend(frameon=False, fontsize=20)
        plt.tick_params(width=2, length=10, labelsize=24)
        plt.tight_layout()
        plt.savefig(f"{Dir}/output{i+1}.png", bbox_inches='tight')
        plt.clf()

makeFig2()
