import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob

def makeFig(fileLocal, saveDir):
    fileName = os.path.splitext(os.path.basename(fileLocal))[0]
    df = pd.read_csv(fileLocal, header=0, skiprows=2, encoding='UTF8')
    first_df = df[df.keys()[0]] / 1000000
    second_df = df[df.keys()[2]]
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(first_df, second_df, label="Resonance")
    ax.set_xlabel("Frequency (MHz)", fontsize=24)
    ax.set_ylabel("Amplitude (dBm)", fontsize=24)
    ax.legend(frameon=False, fontsize=18)
    ax.tick_params(width=2, length=10, labelsize=24)
    plt.tight_layout()
    plt.savefig(os.path.join(saveDir, fileName + ".png"))
    plt.clf()

dir = "G:\\My Drive\\Research\\B4\\data\\20230326_Resonance"
outDir = dir + "\\output"

fileList = glob(os.path.join(dir, "*.csv"))
for file in fileList:
    makeFig(file, outDir)
