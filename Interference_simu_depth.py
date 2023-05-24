import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from glob import glob

def makeFig(filePath, saveDir):
    fileName = os.path.splitext(os.path.basename(filePath))[0]
    df = pd.read_csv(filePath, header=None, skiprows=66, skipfooter=1, encoding="cp932", engine="python", delim_whitespace=True)
    array = df.values
    plt.figure(figsize=(8, 6))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(array[:, 0], array[:, 1], label="reflectance")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Reflectance (%)")
    plt.xticks(np.arange(450, 651, 10))
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["bottom"].set_position(("outward", 0))
    plt.gca().spines["left"].set_position(("outward", 0))
    plt.tick_params(axis="both", direction="in", length=6, width=1)
    plt.tick_params(axis="x", labelsize=10)
    plt.xlim([450, 650])
    plt.ylim([15,25])
    plt.grid(axis="x", color="grey", linestyle=":", linewidth=0.5)
    plt.savefig(os.path.join(saveDir, f"{fileName}.png"))
    plt.clf()

dir = "G:\\My Drive\\Research\\M1\\data\\20230518_Interference"
outDir = os.path.join(dir, "depth")

fileList = glob(os.path.join(dir, "*.txt"))
for filePath in fileList:
    makeFig(filePath, outDir)
