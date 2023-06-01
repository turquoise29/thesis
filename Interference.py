import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob

def makeFig(filePath, saveDir):
    fileName = os.path.splitext(os.path.basename(filePath))[0]
    df = pd.read_csv(filePath, header=None, skiprows=66, skipfooter=1, encoding="cp932", engine="python", delim_whitespace=True)
    array = df.values
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(array[:, 0], array[:, 1], label="reflectance")
    plt.xlim([400, 800])
    plt.xlabel("Wavelength (nm)", fontsize=18)
    plt.ylabel("Reflectance (%)", fontsize=18)
    #plt.ylim([0, 100])
    plt.ylim([0,40])
    plt.legend(frameon=False, fontsize=18)
    plt.tick_params(width=2, length=10, labelsize=18)
    plt.axvline(x=638, color='red', linestyle='--', label='638nm')
    plt.axvline(x=532, color='green', linestyle='--', label='532nm')


    plt.tight_layout()
    plt.savefig(os.path.join(saveDir, f"{fileName}.png"))
    plt.clf()

dir = "G:\\My Drive\\Research\\M1\\data\\20230526_Interference"
outDir = os.path.join(dir, "output")


fileList = glob(os.path.join(dir, "*.txt"))
for filePath in fileList:
    makeFig(filePath, outDir)
