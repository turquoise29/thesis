import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

Dir = "G:/My Drive/Research/M1/data/20230529_Raman_G-2D"

def makeFig2():
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    plt.figure(figsize=(10, 8))
    plot = plt.subplot()
    
    for file in sorted(glob.glob(Dir + "/*.xlsx")):
        array = pd.read_excel(file, header=None, skiprows=1)
        label = "strain" if os.path.splitext(os.path.basename(file))[0][0] == "s" else "no strain"
        plt.scatter(array.iloc[:, 1], array.iloc[:, 2], label=label)
    plt.xlabel("G frequency (cm$^{-1}$)", fontsize=20)
    plt.ylabel("2D frequency (cm$^{-1}$)", fontsize=20)
    plt.xlim(1567, 1590)  # x軸の範囲を設定
    plt.ylim(2667, 2690)  # y軸の範囲を設定
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=20)
    plt.tick_params(labelsize=20)
    plt.tight_layout()
    plot.set_aspect('equal')

    plt.locator_params(axis='x', nbins=6)
    plt.locator_params(axis='y', nbins=6)


    plt.savefig(os.path.join(Dir, "output.png"), bbox_inches='tight')
    plt.clf()

makeFig2()
