import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def makeFig(fileList, saveDir):
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    x_min = float('inf')
    x_max = float('-inf')

    for i, fileLocal in enumerate(fileList):
        fileName = os.path.splitext(os.path.basename(fileLocal))[0]
        df = pd.read_excel(fileLocal, header=0, skiprows=2)
        first_df = df[df.columns[0]] / 1000000
        second_df = df[df.columns[1]]

        label = "Atmospheric" if "Atmospheric" in fileName else "Vacuum"
        ax.plot(first_df, second_df, label=label, color=colors[i % len(colors)])
        x_min = min(x_min, min(first_df))
        x_max = max(x_max, max(first_df))

    ax.set_xlabel("Frequency (MHz)", fontsize=24)
    ax.set_ylabel("Amplitude (dBm)", fontsize=24)
    ax.legend(frameon=True, fontsize=24)
    ax.tick_params(width=2, length=10, labelsize=24)
    
    
    x_ticks = np.linspace(x_min, x_max, num=5)
    ax.set_xticks(x_ticks)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xticks(fontsize=20)
    ax.set_ylim(-80, -45)
    plt.tight_layout()
    plt.savefig(os.path.join(saveDir, "output.png"))
    plt.clf()

dir = "G:\\My Drive\\Research\\M1\\data\\20230620_Resonance_APnostrain"
outDir = dir

fileList = glob(os.path.join(dir, "*.xlsx"))
makeFig(fileList, outDir)
