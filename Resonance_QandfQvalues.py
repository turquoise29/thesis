import pandas as pd
import os
import numpy as np
from glob import glob

def calculate_resonant_frequency_Q(csv_file):
    data = pd.read_csv(csv_file, header=0, skiprows=2, encoding='UTF8')
    frequencies = data.iloc[:, 0].values.astype(float) 
    amplitudes_dBm = data.iloc[:, 2].values.astype(float) 
    max_amplitude_index = np.argmax(amplitudes_dBm)
    resonant_frequency = frequencies[max_amplitude_index]
    half_power_amplitude = amplitudes_dBm[max_amplitude_index] - 3 
    indices_left = np.where(amplitudes_dBm[:max_amplitude_index] <= half_power_amplitude)[0]
    indices_right = np.where(amplitudes_dBm[max_amplitude_index:] <= half_power_amplitude)[0] + max_amplitude_index
    left_index = indices_left[-1] if len(indices_left) > 0 else 0
    right_index = indices_right[0] if len(indices_right) > 0 else len(frequencies) - 1
    delta_f = frequencies[right_index] - frequencies[left_index]
    q_value = resonant_frequency / delta_f

    return resonant_frequency, q_value

dir = "G:\\My Drive\\Research\\B4\\data\\20220623_Resonance2"

csv_files = glob(os.path.join(dir, "*.csv"))
results = []

for csv_file in csv_files:
    resonant_frequency, q_value = calculate_resonant_frequency_Q(csv_file)
    file_name = os.path.basename(csv_file)
    results.append({'CSV File': file_name, 'Resonant Frequency': resonant_frequency, 'Q Value': q_value})

df = pd.DataFrame(results)

output_file = os.path.join(dir, 'Q_results.xlsx')
df.to_excel(output_file, index=False)
