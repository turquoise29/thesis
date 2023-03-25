from cv2 import dft
import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob


def makeFig(fileLocal, saveDir):
    fileName = os.path.splitext(os.path.basename(fileLocal))[0]
    df = pd.read_csv(fileLocal, header = 0, skiprows = 2, encoding = 'UTF8')
    first_df = df[df.keys()[0]] /1000000
    second_df = df[df.keys()[2]]
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(first_df, second_df
                #, color = "m"
            )
    plt.xlabel("Frequency (MHz)", fontsize=24)
    plt.ylabel("Amplitude (dBm)", fontsize=24)
    #plt.legend(frameon=False, fontsize=18)
    #plt.xlim(12.8,12.9)
    plt.tick_params(width = 2, length = 10,labelsize=24)
    plt.tight_layout()
    plt.savefig(saveDir + "/" + fileName + ".png")
    plt.clf()
###########################################################################################

dir = "G:\\My Drive\\Research\\B4\\data\\20230325_Resonance"
outDir = "G:\\My Drive\\Research\\B4\\data\\20230325_Resonance\\output"

###########################################################################################

fileList = glob(dir + "/*.csv")
for file in fileList:
    makeFig(file, outDir)
