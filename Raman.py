import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


def makeFig(file_path, save_dir):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(file_path, header=None, skiprows=19, skipfooter=47, encoding="shift-jis", engine='python')
    x, y = df[0], df[1]
    plt.plot(x, y)
    plt.xlim(1000, 3000)
    plt.xlabel("Raman shift (cm$^{-1}$)", fontsize=14)
    plt.ylabel("Intensity (a.u.)", fontsize=14)
    plt.tick_params(width=2, length=10, labelsize=14, direction="in")
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, file_name + ".png"), bbox_inches='tight')
    plt.clf()

dir = "G:\\My Drive\\Research\\M1\\data\\20230721_Raman_StrainField-4month-C9&10"
outdir = os.path.join(dir, "graph")

file_list = glob.glob(os.path.join(dir, "*.csv"))
for file_path in file_list:
    makeFig(file_path, outdir)
