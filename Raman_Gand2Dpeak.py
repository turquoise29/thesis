import os
import glob
import pandas as pd

def find_peaks(file_path):
    try:
        df = pd.read_csv(file_path, header=None, skiprows=30, skipfooter=50, encoding="shift-jis", engine='python')
        x, y = df[0], df[1]

        g_peak = x[(x >= 1570) & (x <= 1600)][y[(x >= 1570) & (x <= 1600)].idxmax()]
        d_peak = x[(x >= 2660) & (x <= 2690)][y[(x >= 2660) & (x <= 2690)].idxmax()]

        return g_peak, d_peak
    except (pd.errors.ParserError, pd.errors.EmptyDataError):
        # データ読み込み時のエラーが発生した場合や空のファイルの場合は None を返す
        return None, None

dir = "G:\\My Drive\\Research\\M1\\data\\20230531_Raman_SensorSimposium"
file_list = glob.glob(os.path.join(dir, "*.csv"))

results = []

for file_path in file_list:
    g_peak, d_peak = find_peaks(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    if g_peak is not None and d_peak is not None:
        result = {
            "File": file_name,
            "G peak": g_peak,
            "2D peak": d_peak
        }
        results.append(result)

output_dir = dir
os.makedirs(output_dir, exist_ok=True)
output_csv_path = os.path.join(output_dir, "G-2DpeakValues.csv")

df_results = pd.DataFrame(results)
df_results.to_csv(output_csv_path, index=False)

# 平均値を計算
g_peak_avg = df_results["G peak"].mean()
d_peak_avg = df_results["2D peak"].mean()

# 平均値をデータフレームに追加
avg_result = {
    "File": "Average",
    "G peak": g_peak_avg,
    "2D peak": d_peak_avg
}
df_avg = pd.DataFrame([avg_result])

# CSVファイルとして平均値を追加
df_results_avg = pd.concat([df_results, df_avg], ignore_index=True)
df_results_avg.to_csv(output_csv_path, index=False)

# CSVからExcelに変換
output_excel_path = os.path.join(output_dir, "G-2DpeakAverage.xlsx")
with pd.ExcelWriter(output_excel_path) as writer:
    df_results_avg.to_excel(writer, index=False, sheet_name="Data")

# CSVファイルを削除
os.remove(output_csv_path)
