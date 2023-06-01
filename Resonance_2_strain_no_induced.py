import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path

Dir = "G:\\My Drive\\Research\\M1\\data\\20230601_Resonance_strain-no-induced"

def makeFig2():
    files = sorted(glob.glob(Dir + "/*.csv"))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    fig, [ax, ax2] = plt.subplots(1, 2,sharey='row', sharex='col', figsize=(8, 4))

    for file in files:
        array = pd.read_csv(file,header = 0, skiprows = 2, encoding = 'UTF8').values
        fileName = os.path.splitext(os.path.basename(file))[0]
        if(fileName[0]=="s"):
            kikaku1 = (array[:,2] - min(array[:,2]))/(max(array[:,2])-min(array[:,2]))
            ax2.plot(array[:, 0]/1000000, kikaku1,color = "b", label="Strain-Induced")
        else:
            kikaku3 = (array[:,2] - min(array[:,2]))/(max(array[:,2])-min(array[:,2]))
            ax.plot(array[:, 0]/1000000, kikaku3, color="r", label="No Strain")

    ax.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.tick_params(width = 2, length = 10,labelleft=False, labelright=False, left=False, right=False,labelsize=14)
    ax.tick_params(width = 2, length = 10,labelright=False, right=False,labelsize=14)
    ax.legend(frameon=False, fontsize=18, loc='lower center', bbox_to_anchor=(.5, 1.1))
    ax2.legend(frameon=False, fontsize=18, loc='lower center', bbox_to_anchor=(.5, 1.1))
    ax.tick_params(width=2, length=10, labelsize=14)
    ax2.tick_params(width=2, length=10, labelsize=14)
    plt.tight_layout()


    nami(ax,ax2)

    fig.text(0.5, -0.1, 'Frequency(MHz)', ha='center', va='center', fontsize=17)
    ax.set_ylabel("Amplitude(a.u.)",fontsize=17)
    plt.subplots_adjust(wspace=0.0)
    fig.savefig(Dir + "/output" + ".png", bbox_inches='tight')
    plt.clf()

def nami(ax,ax2):
    # ニョロ波の設定
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

makeFig2()