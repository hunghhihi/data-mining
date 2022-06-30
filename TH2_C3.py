import pandas as pd

df = pd.read_csv('datasets/Full_Mark_2020.csv')

print("-----HA NOI------")

hanoi_df = df.loc[df['city'] == '01']
hanoi_df['tongdiem'] = hanoi_df['Toan'] + \
    hanoi_df['Nguvan'] + hanoi_df['Ngoaingu']
hanoi_df.to_csv('datasets/Hanoi_Mark_2020.csv', index=False)

print(hanoi_df.count())
print(hanoi_df["Toan"].describe())
print(hanoi_df["Toan"].median())
print(hanoi_df["Toan"].mode())
print(hanoi_df["tongdiem"].describe())
print(hanoi_df["tongdiem"].median())
print(hanoi_df["tongdiem"].mode())

"""
    Số lượng thí sinh dự thi: 24044
    Điểm trung bình môn toán: 6.74
    Điểm trung vị môn toán: 7.2
    Độ lệch chuẩn môn toán: 1.94
    Mode môn toán: 8.4
    Điểm trung bình tổng điểm: 17.89
    Điểm trung vị tổng điểm: 17.9
    Độ lệch chuẩn tổng điểm: 3.82
    Mode tổng điểm: 18
"""
print("-----TP HCM------")

hcm_df = df.loc[df['city'] == '02']
hcm_df['tongdiem'] = hcm_df['Toan'] + hcm_df['Nguvan'] + hcm_df['Ngoaingu']
hcm_df.to_csv('datasets/Hcm_Mark_2020.csv', index=False)

print(hcm_df.count())
print(hcm_df["Toan"].describe())
print(hcm_df["Toan"].median())
print(hcm_df["Toan"].mode())
print(hcm_df["tongdiem"].describe())
print(hcm_df["tongdiem"].median())
print(hcm_df["tongdiem"].mode())

"""
    Số lượng thí sinh dự thi: 24167
    Điểm trung bình môn toán: 7.19
    Điểm trung vị môn toán: 7.4
    Độ lệch chuẩn môn toán: 1.43
    Mode môn toán: 7.6
    Điểm trung bình tổng điểm: 20.2
    Điểm trung vị tổng điểm: 20.3
    Độ lệch chuẩn tổng điểm: 2.75
    Mode tổng điểm: 20
"""
