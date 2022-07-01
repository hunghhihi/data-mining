from math import isnan
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/Extended_Full_Mark_2020.csv')

print(f"số học sinh rớt: {df.groupby('XepLoai')['Code'].count()['rot']}")
print(
    f"số học sinh trung bình: {df.groupby('XepLoai')['Code'].count()['trungbinh']}")
print(f"số học sinh khá: {df.groupby('XepLoai')['Code'].count()['kha']}")
print(f"số học sinh giỏi: {df.groupby('XepLoai')['Code'].count()['gioi']}")

"""
số học sinh rớt: 132920
số học sinh trung bình: 812208
số học sinh khá: 82298
số học sinh giỏi: 24434
"""

# Vẽ biểu đồ
fig = plt.figure(figsize=(12, 6))
xep_loai = fig.add_subplot(121)
xep_loai.set_title('Xếp loại')
xep_loai.hist(df['XepLoai'], bins=80)

diem_trung_binh = fig.add_subplot(122)
diem_trung_binh.set_title('Điểm trung bình')
diem_trung_binh.hist(df['DiemTrungBinh'], bins=80)

plt.show()
