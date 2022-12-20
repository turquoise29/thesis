from cv2 import dft
import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob


def makeFig(fileLocal, saveDir):
    fileName = os.path.splitext(os.path.basename(fileLocal))[0]
    df = pd.read_csv(fileLocal, header=None, skiprows = 19, skipfooter=46, encoding = "shift-jis", engine='python')
    first_df = df[df.keys()[0]] 
    second_df = df[df.keys()[1]]
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.plot(first_df, second_df, label="raman")
    plt.xlim(1000,3000)
    plt.xlabel("Raman shift (cm$^{-1}$)")
    plt.ylabel("Intensity (a.u.)")
    #plt.ylim(0,50)
    plt.tick_params(width = 2, length = 10,labelsize=24)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(saveDir + "/" + fileName + ".png", bbox_inches='tight')
    plt.clf()


###########################################################################################

dir = "G:\\My Drive\\Research\\data\\20221213_Raman"
outDir = "G:\\My Drive\\Research\\data\\20221213_Raman\\graph"

###########################################################################################

fileList = glob(dir + "/*.csv")
for file in fileList:
    makeFig(file, outDir)
