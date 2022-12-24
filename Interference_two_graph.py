import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

Dir = "G:\\My Drive\\Research\\data\\20220618_Interference"

def makeFig2():
    files = sorted(glob.glob(Dir + "/*.txt"))
    file_number = len(files)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    for file in files:
        array = pd.read_table(file,header=None,skiprows=66,skipfooter=1, encoding="cp932",engine="python").values
        fileName = os.path.splitext(os.path.basename(file))[0]
        if(fileName[0]=="k"):
            plt.plot(array[:, 0], array[:, 1], label="no graphene",color='red')
        else:
            plt.plot(array[:, 0], array[:, 1], label="suspended graphene")
    plt.xlim(400,800)
    plt.xlabel("Wavelength (nm)",fontsize=14)
    plt.ylabel("Reflectance (%)",fontsize=14)
    plt.ylim(0,40)
    plt.legend(frameon=False
    #,bbox_to_anchor=(1, 0)
    #, loc='lower right'
    #, borderaxespad=1
    , fontsize=20)
    plt.tick_params(width = 2, length = 10,labelsize=24)
    plt.tight_layout()
    plt.savefig(Dir + "/output" + ".png", bbox_inches='tight')
    plt.clf()

makeFig2()