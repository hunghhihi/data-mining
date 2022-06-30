import pandas as pd

df = pd.read_csv('datasets/Full_Mark_2020.csv')

print(df['Toan'].describe())
print(df['Toan'].median())
print(df['Toan'].mode())

"""
    Kết quả:
    Điểm trung bình (mean): 6.7
    Điểm trung vị (median): 7.0
    mode: 8.0
    Độ lệch chuẩn (std): 1.8
"""
