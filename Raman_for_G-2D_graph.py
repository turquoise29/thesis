import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

Dir = "G:/My Drive/Research/M1/data/20230529_Raman_G-2D"

def makeFig2():
    plt.figure(figsize=(7, 7))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    for file in sorted(glob.glob(Dir + "/*.xlsx")):
        array = pd.read_excel(file, header=None, skiprows=1)
        label = "strain" if os.path.splitext(os.path.basename(file))[0][0] == "s" else "no strain"
        plt.scatter(array.iloc[:, 1], array.iloc[:, 2], label=label)
    plt.xlabel("G frequency (cm$^{-1}$)", fontsize=20)
    plt.ylabel("2D frequency (cm$^{-1}$)", fontsize=20)
    plt.xlim(1570, 1610)  # x軸の範囲を設定
    plt.ylim(2655, 2710)  # y軸の範囲を設定
    plt.legend(frameon=True, fontsize=20)
    plt.tick_params(width=2, length=10, labelsize=20)
    plt.tight_layout()
    plt.savefig(os.path.join(Dir, "output.png"), bbox_inches='tight')
    plt.clf()

makeFig2()
