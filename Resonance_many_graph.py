import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path

Dir = "G:\\My Drive\\Research\\B4\\data\\20230102_Resonance"

def makeFig3():
    files = sorted(glob.glob(Dir + "/*.csv"))
    file_number = len(files)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    fig, [ax, ax2, ax3] = plt.subplots(1, 3,sharey='row', sharex='col', figsize=(8, 2))
    for file in files:
        array = pd.read_csv(file,header = 0, skiprows = 2, encoding = 'UTF8').values
        fileName = os.path.splitext(os.path.basename(file))[0]
        if(fileName[0]=="s"):
            kikaku1 = (array[:,2] - min(array[:,2]))/(max(array[:,2])-min(array[:,2]))
            ax3.plot(array[:, 0]/1000000, kikaku1,color = "b")
        if(fileName[0]=="m"):
            kikaku2 = (array[:,2] - min(array[:,2]))/(max(array[:,2])-min(array[:,2]))
            ax2.plot(array[:, 0]/1000000, kikaku2, color="y")
        else:
            kikaku3 = (array[:,2] - min(array[:,2]))/(max(array[:,2])-min(array[:,2]))
            ax.plot(array[:, 0]/1000000, kikaku3, color="r")
    
    ax.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    ax2.tick_params(width = 2, length = 10,labelleft=False, labelright=False, left=False, right=False,labelsize=14)
    ax.tick_params(width = 2, length = 10,labelright=False, right=False,labelsize=14)
    ax3.tick_params(width = 2, length = 10,labelleft=False, left=False,labelsize=14)
    ax.set_xlim(11.76,11.96)
    ax2.set_xlim(12.78,12.9)
    #ax.set_xticks([11.86])
    ax2.set_xticks([12.80,12.85])
    #ax3.set_xticks([14.89])
    ax3.set_xlim(14.79,14.99)
    nami(ax,ax2)
    nami(ax2,ax3)
    ax2.set_xlabel("Frequency(MHz)",fontsize=18)
    ax.set_ylabel("Amplitude(a.u.)",fontsize=17)
    plt.subplots_adjust(wspace=0.0)
    fig.savefig(Dir + "/output" + ".png", bbox_inches='tight')
    plt.clf()

def nami(ax,ax2):
    d1 = 0.02 # y軸のはみだし量
    d2 = 0.03 # ニョロ波の高さ
    wn = 21   # ニョロ波の数（奇数値を指定）
    pp = (0,d2,0,-d2)
    px = np.array([1+pp[i%4] for i in range(0,wn)])
    py = np.linspace(-d1,1+d1,wn)
    p = Path(list(zip(px,py)), [Path.MOVETO]+[Path.CURVE3]*(wn-1))
    line1 = mpatches.PathPatch(p, lw=4, edgecolor='black',
                            facecolor='None', clip_on=False,
                            transform=ax.transAxes, zorder=10)
    line2 = mpatches.PathPatch(p,lw=3, edgecolor='white',
                            facecolor='None', clip_on=False,
                            transform=ax.transAxes, zorder=10,
                            capstyle='round')
    a = ax2.add_patch(line1)
    a = ax2.add_patch(line2)

makeFig3()