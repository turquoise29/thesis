import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob

def makeFig(fileLocal, saveDir):
    fileName = os.path.splitext(os.path.basename(fileLocal))[0]
    df = pd.read_table(fileLocal,header=None,skiprows=66,skipfooter=1, encoding="cp932",engine="python")
    array = df.values
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(array[:, 0], array[:, 1], label="reflectance")
    plt.xlim(400,800)
    plt.xlabel("Wavelength (nm)", fontsize=18)
    plt.ylabel("Reflectance (%)", fontsize=18)
    plt.ylim(0,40)
    plt.legend(frameon=False,fontsize=18)
    plt.tick_params(width = 2, length = 10,labelsize=18)
    plt.tight_layout()
    plt.savefig(saveDir + "/" + fileName + ".png")
    plt.clf()
###########################################################################################

dir = "G:\\My Drive\\Research\\\B4\\data\\20230321_Interference"
outDir = "G:\\My Drive\\Research\\B4\\data\\20230321_Interference\\output"

###########################################################################################

fileList = glob(dir + "/*.txt")
for file in fileList:
    makeFig(file, outDir)