import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
from cv2 import dft

Dir = "G:\\My Drive\\Research\\M1\\data\\20230427_Raman_sensor"
outDir = Dir

def makeFig2():
    files = sorted(glob.glob(Dir + "/*.csv"))
    file_number = len(files)
    #plt.figure(figsize=(10,5), dpi=50)
    #plt.figure(figsize=(6,4), dpi=50)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    for file in files:
        array = pd.read_csv(file, header=None, skiprows = 19, skipfooter=47, encoding = "shift-jis", engine='python').values
        fileName = os.path.splitext(os.path.basename(file))[0]
        if(fileName[0]=="k"):
            kikaku1 = (array[:,1] - min(array[:,1]))/(max(array[:,1])-min(array[:,1]))
            plt.plot(array[:, 0], kikaku1
            , label="no strain"
            ,color='b')
        else:
            kikaku2 = (array[:,1] - min(array[:,1]))/(max(array[:,1])-min(array[:,1]))
            plt.plot(array[:, 0], kikaku2
            , label="strain management"
            ,color="r"
            )
    #plt.xlim(1500,2800)
    #plt.xlim(2625,2700) #2Dピーク
    plt.xlim(1550,1600) #Gピーク 
    plt.xlabel("Raman shift (cm$^{-1}$)",fontsize=24)
    plt.ylabel("Intensity (a.u.)",fontsize=24)
    plt.legend(frameon=False, fontsize=20)
    plt.tick_params(width = 2, length = 10,labelsize=24)
    plt.tight_layout()
    plt.savefig(outDir + "/output" + ".png", bbox_inches='tight')
    plt.clf()

makeFig2()